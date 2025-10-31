#!/bin/bash

###############################################################################
# ZIM Tools Installation Script
# 
# This script installs ZIM tools (zimwriterfs, zimcheck, etc.) on various
# Linux distributions. Supports Ubuntu/Debian, CentOS/RHEL, Arch Linux,
# and provides Docker alternatives.
#
# Usage: ./install_zim_tools.sh [options]
# Options:
#   --distribution <distro>    Specify distribution (auto-detect default)
#   --install-type <type>      Installation type: package, source, docker
#   --help, -h                Show this help message
###############################################################################

set -e  # Exit on any error

# Script configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Installation options
DISTRIBUTION=""
INSTALL_TYPE=""
FORCE_INSTALL=false
VERBOSE=false

# Default installation type based on distribution
DEFAULT_INSTALL_TYPE="package"

###############################################################################
# Utility Functions
###############################################################################

log() {
    local level="$1"
    shift
    local message="$*"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    case "$level" in
        "INFO")
            echo -e "${GREEN}[INFO]${NC} $timestamp: $message"
            ;;
        "WARN")
            echo -e "${YELLOW}[WARN]${NC} $timestamp: $message"
            ;;
        "ERROR")
            echo -e "${RED}[ERROR]${NC} $timestamp: $message"
            ;;
        "DEBUG")
            if [ "$VERBOSE" = true ]; then
                echo -e "${BLUE}[DEBUG]${NC} $timestamp: $message"
            fi
            ;;
    esac
}

show_help() {
    cat << EOF
ZIM Tools Installation Script

Usage: $0 [OPTIONS]

Options:
    --distribution <distro>     Distribution: ubuntu, debian, centos, rhel, arch, alpine, auto
    --install-type <type>       Installation type: package, source, docker, auto
    --force, -f                 Force installation even if already present
    --verbose, -v               Enable verbose output
    --help, -h                  Show this help message

Distribution Examples:
    ubuntu, debian, centos, rhel, arch, alpine, auto (detect)

Installation Types:
    package  - Install via system package manager
    source   - Build from source code
    docker   - Use Docker container
    auto     - Use default for distribution

Examples:
    $0                             # Auto-detect and install
    $0 --distribution ubuntu       # Install on Ubuntu via apt
    $0 --install-type docker       # Use Docker method
    $0 --force --verbose           # Force re-installation with verbose output

EOF
}

detect_distribution() {
    if [ ! -z "$DISTRIBUTION" ] && [ "$DISTRIBUTION" != "auto" ]; then
        echo "$DISTRIBUTION"
        return 0
    fi
    
    # Auto-detect distribution
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        case "$ID" in
            ubuntu|debian)
                echo "$ID"
                ;;
            centos|rhel|fedora)
                if command -v dnf >/dev/null 2>&1; then
                    echo "fedora"
                else
                    echo "centos"
                fi
                ;;
            arch|manjaro)
                echo "arch"
                ;;
            alpine)
                echo "alpine"
                ;;
            *)
                echo "unknown"
                ;;
        esac
    elif command -v lsb_release >/dev/null 2>&1; then
        local distro=$(lsb_release -si | tr '[:upper:]' '[:lower:]')
        case "$distro" in
            ubuntu|debian|centos|rhel|fedora|arch|alpine)
                echo "$distro"
                ;;
            *)
                echo "unknown"
                ;;
        esac
    else
        echo "unknown"
    fi
}

detect_install_type() {
    local distro="$1"
    
    if [ ! -z "$INSTALL_TYPE" ] && [ "$INSTALL_TYPE" != "auto" ]; then
        echo "$INSTALL_TYPE"
        return 0
    fi
    
    # Default installation type based on distribution
    case "$distro" in
        ubuntu|debian)
            echo "package"
            ;;
        centos|rhel|fedora)
            echo "package"
            ;;
        arch)
            echo "package"
            ;;
        alpine)
            echo "package"
            ;;
        *)
            # For unknown systems, try package first, then docker as fallback
            echo "package"
            ;;
    esac
}

check_existing_installation() {
    log "INFO" "Checking for existing ZIM tools installation..."
    
    if command -v zimwriterfs >/dev/null 2>&1; then
        local version=$(zimwriterfs --version 2>/dev/null || echo "unknown")
        log "INFO" "Found existing zimwriterfs installation: $version"
        
        if [ "$FORCE_INSTALL" = true ]; then
            log "INFO" "Force installation requested, proceeding with installation"
            return 0
        else
            log "INFO" "ZIM tools already installed. Use --force to re-install."
            return 1
        fi
    else
        log "INFO" "No existing ZIM tools installation found"
        return 0
    fi
}

###############################################################################
# Installation Functions
###############################################################################

install_package_ubuntu() {
    log "INFO" "Installing ZIM tools on Ubuntu/Debian via apt..."
    
    # Update package lists
    sudo apt update
    
    # Install zim-tools package
    sudo apt install -y zim-tools
    
    # Verify installation
    if command -v zimwriterfs >/dev/null 2>&1; then
        local version=$(zimwriterfs --version 2>/dev/null || echo "unknown")
        log "INFO" "Successfully installed ZIM tools: $version"
        return 0
    else
        log "ERROR" "Failed to install ZIM tools via apt"
        return 1
    fi
}

install_package_centos() {
    log "INFO" "Installing ZIM tools on CentOS/RHEL via yum..."
    
    # Try yum first (older systems)
    if command -v yum >/dev/null 2>&1; then
        sudo yum install -y zim-tools || {
            log "WARN" "yum installation failed, trying dnf..."
            sudo dnf install -y zim-tools
        }
    else
        # Use dnf for newer systems
        sudo dnf install -y zim-tools
    fi
    
    # Verify installation
    if command -v zimwriterfs >/dev/null 2>&1; then
        local version=$(zimwriterfs --version 2>/dev/null || echo "unknown")
        log "INFO" "Successfully installed ZIM tools: $version"
        return 0
    else
        log "ERROR" "Failed to install ZIM tools via yum/dnf"
        return 1
    fi
}

install_package_arch() {
    log "INFO" "Installing ZIM tools on Arch Linux via pacman..."
    
    # Update package database
    sudo pacman -Sy
    
    # Install zim-tools package
    sudo pacman -S --noconfirm zim-tools
    
    # Verify installation
    if command -v zimwriterfs >/dev/null 2>&1; then
        local version=$(zimwriterfs --version 2>/dev/null || echo "unknown")
        log "INFO" "Successfully installed ZIM tools: $version"
        return 0
    else
        log "ERROR" "Failed to install ZIM tools via pacman"
        return 1
    fi
}

install_package_alpine() {
    log "INFO" "Installing ZIM tools on Alpine Linux via apk..."
    
    # Update package index
    sudo apk update
    
    # Install zim-tools package
    sudo apk add zim-tools
    
    # Verify installation
    if command -v zimwriterfs >/dev/null 2>&1; then
        local version=$(zimwriterfs --version 2>/dev/null || echo "unknown")
        log "INFO" "Successfully installed ZIM tools: $version"
        return 0
    else
        log "ERROR" "Failed to install ZIM tools via apk"
        return 1
    fi
}

install_source() {
    log "INFO" "Installing ZIM tools from source..."
    
    # Install build dependencies
    log "INFO" "Installing build dependencies..."
    
    case "$(detect_distribution)" in
        ubuntu|debian)
            sudo apt update
            sudo apt install -y build-essential meson ninja-build pkg-config
            sudo apt install -y libzim-dev libmagic-dev zlib1g-dev libgumbo-dev libicu-dev
            ;;
        centos|rhel|fedora)
            if command -v dnf >/dev/null 2>&1; then
                sudo dnf groupinstall -y "Development Tools"
                sudo dnf install -y meson ninja-build pkgconfig
                sudo dnf install -y libzim-devel file-devel zlib-devel gumbo-parser-devel icu-devel
            else
                sudo yum groupinstall -y "Development Tools"
                sudo yum install -y meson ninja-build pkgconfig
                sudo yum install -y libzim-devel file-devel zlib-devel gumbo-parser-devel icu-devel
            fi
            ;;
        arch)
            sudo pacman -Sy --noconfirm base-devel meson ninja
            sudo pacman -S --noconfirm libzim libmagic zlib gumbo-parser icu
            ;;
        alpine)
            sudo apk add --no-cache build-base meson ninja pkgconfig
            sudo apk add --no-cache libzim-dev file-dev zlib-dev gumbo-parser-dev icu-dev
            ;;
        *)
            log "ERROR" "Unknown distribution for source installation"
            return 1
            ;;
    esac
    
    # Clone and build zim-tools
    log "INFO" "Cloning zim-tools repository..."
    
    local build_dir="/tmp/zim-tools-build"
    rm -rf "$build_dir"
    git clone https://github.com/openzim/zim-tools.git "$build_dir"
    
    cd "$build_dir"
    
    log "INFO" "Building zim-tools..."
    meson build
    ninja -C build
    
    log "INFO" "Installing zim-tools..."
    sudo ninja -C build install
    
    # Update library cache
    sudo ldconfig
    
    # Clean up
    cd /
    rm -rf "$build_dir"
    
    # Verify installation
    if command -v zimwriterfs >/dev/null 2>&1; then
        local version=$(zimwriterfs --version 2>/dev/null || echo "unknown")
        log "INFO" "Successfully installed ZIM tools from source: $version"
        return 0
    else
        log "ERROR" "Failed to install ZIM tools from source"
        return 1
    fi
}

install_docker() {
    log "INFO" "Setting up Docker-based ZIM tools..."
    
    # Check if Docker is available
    if ! command -v docker >/dev/null 2>&1; then
        log "ERROR" "Docker is not installed. Please install Docker first."
        return 1
    fi
    
    # Pull official zim-tools image
    log "INFO" "Pulling official zim-tools Docker image..."
    docker pull openzim/zim-tools:latest
    
    # Test the installation
    log "INFO" "Testing zim-tools in Docker container..."
    docker run --rm openzim/zim-tools:latest zimwriterfs --help >/dev/null 2>&1
    
    if [ $? -eq 0 ]; then
        log "INFO" "Successfully set up Docker-based ZIM tools"
        
        # Create wrapper script for convenience
        local wrapper_script="$ROOT_DIR/scripts/zim-docker-wrapper.sh"
        cat > "$wrapper_script" << 'EOF'
#!/bin/bash
# Docker wrapper for ZIM tools

CONTAINER_IMAGE="openzim/zim-tools:latest"

# Parse command line arguments
TOOL=""
ARGS=()

while [[ $# -gt 0 ]]; do
    case $1 in
        zimwriterfs|zimcheck|zimdump|zimsplit)
            TOOL="$1"
            shift
            ;;
        *)
            ARGS+=("$1")
            shift
            ;;
    esac
done

if [ -z "$TOOL" ]; then
    echo "Usage: $0 <tool> [args...]"
    echo "Tools: zimwriterfs, zimcheck, zimdump, zimsplit"
    exit 1
fi

# Run the tool in Docker
docker run --rm -v "$(pwd):/work" "$CONTAINER_IMAGE" "$TOOL" "${ARGS[@]}"
EOF
        
        chmod +x "$wrapper_script"
        log "INFO" "Created Docker wrapper script: $wrapper_script"
        log "INFO" "Usage: $wrapper_script zimwriterfs [options] <source_dir> <output.zim>"
        
        return 0
    else
        log "ERROR" "Failed to test Docker-based ZIM tools"
        return 1
    fi
}

###############################################################################
# Main Script Logic
###############################################################################

main() {
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --distribution)
                DISTRIBUTION="$2"
                shift 2
                ;;
            --install-type)
                INSTALL_TYPE="$2"
                shift 2
                ;;
            --force|-f)
                FORCE_INSTALL=true
                shift
                ;;
            --verbose|-v)
                VERBOSE=true
                shift
                ;;
            --help|-h)
                show_help
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    log "INFO" "Starting ZIM tools installation"
    log "INFO" "Distribution: ${DISTRIBUTION:-auto}"
    log "INFO" "Install type: ${INSTALL_TYPE:-auto}"
    log "INFO" "Force install: $FORCE_INSTALL"
    log "INFO" "Verbose mode: $VERBOSE"
    
    # Check for existing installation
    if ! check_existing_installation; then
        log "INFO" "Installation cancelled - existing installation found"
        exit 0
    fi
    
    # Detect distribution and installation type
    DETECTED_DISTRO=$(detect_distribution)
    DETECTED_TYPE=$(detect_install_type "$DETECTED_DISTRO")
    
    log "INFO" "Detected distribution: $DETECTED_DISTRO"
    log "INFO" "Detected installation type: $DETECTED_TYPE"
    
    # Override with user preferences if specified
    DISTRO_TO_USE="${DISTRO:-$DETECTED_DISTRO}"
    TYPE_TO_USE="${INSTALL_TYPE:-$DETECTED_TYPE}"
    
    # Check for unsupported combinations
    if [ "$DISTRO_TO_USE" = "unknown" ] && [ "$TYPE_TO_USE" = "package" ]; then
        log "WARN" "Unknown distribution detected. Falling back to Docker installation."
        TYPE_TO_USE="docker"
    fi
    
    log "INFO" "Proceeding with: $DISTRO_TO_USE using $TYPE_TO_USE"
    
    # Execute installation
    case "$TYPE_TO_USE" in
        "package")
            case "$DISTRO_TO_USE" in
                ubuntu|debian)
                    install_package_ubuntu
                    ;;
                centos|rhel|fedora)
                    install_package_centos
                    ;;
                arch)
                    install_package_arch
                    ;;
                alpine)
                    install_package_alpine
                    ;;
                *)
                    log "ERROR" "Package installation not supported for distribution: $DISTRO_TO_USE"
                    log "INFO" "Falling back to Docker installation"
                    install_docker
                    ;;
            esac
            ;;
        "source")
            install_source
            ;;
        "docker")
            install_docker
            ;;
        *)
            log "ERROR" "Unknown installation type: $TYPE_TO_USE"
            show_help
            exit 1
            ;;
    esac
    
    # Final verification
    if command -v zimwriterfs >/dev/null 2>&1; then
        log "INFO" "=========================================="
        log "INFO" "    ZIM TOOLS INSTALLATION COMPLETE"
        log "INFO" "=========================================="
        log "INFO" "zimwriterfs version: $(zimwriterfs --version 2>/dev/null || echo 'unknown')"
        log "INFO" "Available tools: zimwriterfs, zimcheck, zimdump, zimsplit"
        log "INFO" ""
        log "INFO" "Next steps:"
        log "INFO" "1. Run: ./build_zim_packages.sh --help"
        log "INFO" "2. Prepare content directory with index.html and favicon.png"
        log "INFO" "3. Execute: ./build_zim_packages.sh --all"
        log "INFO" "=========================================="
    else
        log "ERROR" "Installation verification failed"
        exit 1
    fi
}

# Run main function if script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi