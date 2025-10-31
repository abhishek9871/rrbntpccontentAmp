# OpenZIM ZIM Build Scripts - Complete Package

## Overview

This repository contains a comprehensive, production-ready system for creating ZIM packages from educational content. It includes automated build scripts, detailed documentation, quality assurance tools, and support for multiple content types.

## Quick Start

### 1. Install ZIM Tools

```bash
# Auto-detect system and install
./scripts/install_zim_tools.sh

# Or specify specific options
./scripts/install_zim_tools.sh --distribution ubuntu --verbose
./scripts/install_zim_tools.sh --install-type docker  # Use Docker approach
```

### 2. Prepare Content

Ensure your content directory contains:
- `index.html` - Main landing page
- `favicon.png` - 48x48 PNG icon
- Well-organized HTML content and media assets
- Valid HTML5 markup with proper relative links

### 3. Build ZIM Packages

```bash
# Make scripts executable
chmod +x scripts/*.sh

# Build all packages
./scripts/build_zim_packages.sh --all

# Or build specific packages
./scripts/build_zim_packages.sh --general-awareness
./scripts/build_zim_packages.sh --science

# Clean build with verbose output
./scripts/build_zim_packages.sh --clean --verbose
```

## System Features

### 🎯 **Package Types Supported**
- **General Awareness**: Complete coverage of culture, economy, geography, history, polity
- **Science & Technology**: Biology, chemistry, physics, environmental science
- **Comprehensive Packages**: All-in-one study materials with bilingual support

### 🛠️ **Build Automation**
- **Intelligent Content Detection**: Automatic analysis of available content
- **Metadata Extraction**: Rich metadata generation from source content
- **Quality Assurance**: Built-in validation and verification
- **Error Handling**: Comprehensive error detection and recovery
- **Progress Tracking**: Real-time build progress with detailed logging

### 📚 **Documentation System**
- **ZIM Creation Guide**: Complete step-by-step instructions
- **Metadata Guide**: Comprehensive metadata management
- **Compression Guide**: Performance optimization techniques
- **Troubleshooting Guide**: Solutions for common issues
- **Best Practices**: Industry-standard procedures

### 🔧 **Quality Assurance**
- **Content Validation**: HTML structure and link checking
- **Metadata Verification**: Completeness and accuracy validation
- **Performance Analysis**: File size and loading time optimization
- **Cross-Platform Testing**: Compatibility verification

### 📦 **Installation Options**
- **Package Managers**: apt, yum, pacman, apk support
- **Source Compilation**: Manual build from Git repository
- **Docker Integration**: Container-based tool usage
- **Cross-Platform**: Linux, macOS, Windows (via WSL)

## Directory Structure

```
openzim/zim-build-scripts/
├── README.md                           # This file
├── scripts/
│   ├── build_zim_packages.sh          # Main build automation
│   ├── install_zim_tools.sh           # Tool installation
│   ├── validate_content.sh            # Content validation
│   ├── extract_metadata.sh            # Metadata extraction
│   ├── quality_check.sh               # Quality assurance
│   └── batch_builder.sh               # Batch processing
├── docs/
│   ├── zim_creation_guide.md          # Complete ZIM guide
│   ├── metadata_and_file_organization.md
│   ├── compression_and_optimization.md
│   ├── troubleshooting_guide.md       # Common issues and solutions
│   └── content_analysis_report.md     # Content analysis
├── examples/
│   ├── sample_content/                # Example content structure
│   ├── template_config/               # Configuration templates
│   └── test_scenarios/                # Test cases
├── metadata/
│   ├── templates/                     # Metadata templates
│   └── schemas/                       # JSON schema definitions
├── output/                            # Generated ZIM packages
└── logs/                              # Build logs and reports
```

## Content Preparation

### Required Structure
```
content/
├── index.html                          # Main page (REQUIRED)
├── favicon.png                         # 48x48 PNG icon (REQUIRED)
├── articles/                           # Article content
├── assets/
│   ├── css/                           # Stylesheets
│   ├── js/                            # JavaScript files
│   └── images/                        # Images and media
└── metadata/                          # Content metadata
```

### Validation Checklist
- ✅ Valid HTML5 markup
- ✅ Relative file paths only
- ✅ 48x48 PNG favicon
- ✅ No external dependencies
- ✅ Proper language metadata
- ✅ Accurate attribution
- ✅ License information

## Command Reference

### Build Script Options

```bash
./scripts/build_zim_packages.sh [OPTIONS]

Options:
  --all, -a              Build all packages
  --general-awareness    Build General Awareness package
  --science             Build Science package  
  --complete            Build Complete package
  --clean, -c           Clean previous builds
  --verbose, -v         Verbose output
  --help, -h            Show help
```

### ZIM Tool Options

```bash
# Basic ZIM creation
zimwriterfs --welcome=index.html --favicon=favicon.png \
    --language=eng --title="Package Title" \
    --description="Description" --creator="Creator" \
    --publisher="Publisher" --withFullTextIndex \
    source_dir output.zim

# Advanced options
zimwriterfs --welcome=index.html --favicon=favicon.png \
    --language=eng --title="Advanced Package" \
    --description="With all options" \
    --creator="Content Team" --publisher="OpenZIM" \
    --tags="education;learning;offline" \
    --name="unique-identifier" \
    --minChunkSize=2048 --inflateHtml \
    --uniqueNamespace --redirects=redirects.tsv \
    --verbose source_dir output.zim
```

### Quality Assurance

```bash
# Verify ZIM package integrity
zimcheck output.zim

# Inspect ZIM contents
zimdump --list output.zim
zimdump --dump output.zim --url "index.html"

# Performance testing
./scripts/quality_check.sh /path/to/content
./scripts/validate_content.sh /path/to/content
```

## Metadata Management

### Essential Metadata
```json
{
  "title": "Package Title",
  "description": "Comprehensive description",
  "language": "eng",
  "creator": "Content Creator",
  "publisher": "OpenZIM Project",
  "tags": ["education", "offline", "learning"],
  "license": "CC BY-SA 3.0",
  "version": "1.0.0"
}
```

### Advanced Features
- **Multi-language Support**: Automatic language detection and metadata
- **Rich Attribution**: Complete source tracking and credits
- **Quality Scoring**: Automated content quality assessment
- **License Validation**: Automated license compatibility checking

## Performance Optimization

### Compression Settings
```bash
# Default settings (recommended)
--minChunkSize=2048

# For small files (faster access)
--minChunkSize=1024

# For large files (better compression)
--minChunkSize=4096

# HTML optimization
--inflateHtml
```

### Content Optimization
- **Image Compression**: Automatic WebP conversion and optimization
- **HTML Minification**: Code compression and optimization
- **CSS/JS Minification**: Automated asset optimization
- **Dead Link Removal**: Detection and cleanup of broken links

## Troubleshooting

### Common Issues

1. **Tool Not Found**
   ```bash
   # Install ZIM tools
   ./scripts/install_zim_tools.sh
   
   # Use Docker approach
   ./scripts/install_zim_tools.sh --install-type docker
   ```

2. **Missing Favicon**
   ```bash
   # Create simple favicon
   convert -size 48x48 xc:blue favicon.png
   ```

3. **HTML Validation Errors**
   ```bash
   # Use tidy for validation
   sudo apt install tidy
   tidy -q -e -o errors.html index.html
   ```

4. **Large File Sizes**
   ```bash
   # Optimize images
   find . -name "*.jpg" -exec jpegoptim --strip-all --max=85 {} \;
   find . -name "*.png" -exec optipng {} \;
   ```

### Debug Mode
```bash
# Enable verbose logging
./scripts/build_zim_packages.sh --verbose

# Check intermediate files
ls -la build/
cat build/zimwriterfs.log
```

## Advanced Usage

### Batch Processing
```bash
# Create batch configuration file
cat > batch_config.csv << EOF
/path/to/content1,Title 1,Description 1,output1.zim
/path/to/content2,Title 2,Description 2,output2.zim
/path/to/content3,Title 3,Description 3,output3.zim
EOF

# Process batch
./scripts/batch_builder.sh batch_config.csv
```

### Custom Templates
```bash
# Use custom HTML template
./scripts/build_zim_packages.sh --template custom-template.html

# Use custom metadata template
./scripts/build_zim_packages.sh --metadata-template custom-metadata.json
```

### Integration with CI/CD
```bash
# GitHub Actions example
- name: Build ZIM Packages
  run: |
    chmod +x scripts/*.sh
    ./scripts/install_zim_tools.sh
    ./scripts/build_zim_packages.sh --clean --all
    ./scripts/quality_check.sh ./output
    
- name: Upload Artifacts
  uses: actions/upload-artifact@v3
  with:
    name: zim-packages
    path: output/*.zim
```

## Contributing

### Development Setup
```bash
# Clone repository
git clone <repository-url>
cd openzim/zim-build-scripts

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
./scripts/run_tests.sh
```

### Adding New Features
1. Follow established code patterns
2. Include comprehensive documentation
3. Add unit tests for new functionality
4. Update this README with usage examples

## License

This project is released under the GNU General Public License v3.0, same as the OpenZIM project. See LICENSE file for details.

## Support

### Documentation
- **Complete Guide**: [docs/zim_creation_guide.md](docs/zim_creation_guide.md)
- **Troubleshooting**: [docs/troubleshooting_guide.md](docs/troubleshooting_guide.md)
- **Metadata Guide**: [docs/metadata_and_file_organization.md](docs/metadata_and_file_organization.md)
- **Optimization**: [docs/compression_and_optimization.md](docs/compression_and_optimization.md)

### Getting Help
- Check the troubleshooting guide for common solutions
- Review build logs for detailed error information
- Validate content using the built-in quality tools
- Consult ZIM format documentation for technical details

## Version History

### v1.0.0 (Current)
- Complete build automation system
- Multi-platform installation support
- Comprehensive documentation
- Quality assurance framework
- Batch processing capabilities
- Advanced metadata management
- Performance optimization tools

## Acknowledgments

- OpenZIM Project for the ZIM format and tools
- Wikipedia for educational content (CC BY-SA 3.0)
- Kiwix project for offline content distribution
- Various open-source tools and libraries used in this system

---

**Ready to create your first ZIM package?** Start with `./scripts/install_zim_tools.sh --help` and follow the quick start guide above!