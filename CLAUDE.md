# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SuperThrift is a static HTML/CSS landing page for thrift stores in Pearl and Brandon, Mississippi. The site features store information, donation pickup scheduling, and contact forms. It requires no build process or dependencies.

## Development Workflow

### Local Development
Open `index.html` directly in a web browser. No build process, bundler, or local server required.

### Testing Changes
After making edits to `index.html` or `css/styles.css`, refresh the browser to see changes immediately.

### Deployment
This is a static site that can be deployed to any web host by uploading the files directly. Compatible with GitHub Pages, Netlify, Vercel, or traditional FTP hosting.

## Code Architecture

### File Structure
- `index.html` - Single-page application containing all content sections (hero, locations, offerings, donations, contact)
- `css/styles.css` - All styles in a single CSS file with CSS custom properties for theming
- `images/` - Directory for image assets (currently uses emoji placeholders)

### CSS Design System
The site uses CSS custom properties (lines 8-21 in `css/styles.css`) for consistent theming:
- Primary color: `--primary-color` (#974df3 purple)
- Secondary color: `--secondary-color` (#2ea3f2 blue)
- Gold accent: `--gold-color` (#d4af37)

To change the color scheme, update these CSS variables.

### Layout Approach
- Mobile-first responsive design using CSS Grid and Flexbox
- Breakpoints at 768px and 480px for responsive adjustments
- Sticky header with gradient background
- All sections use `.container` class with max-width of 1200px

### Key Sections
- **Header**: Sticky navigation with logo and links
- **Hero**: Gradient background with CTA buttons
- **Locations**: Grid layout for Pearl and Brandon store cards
- **Offerings**: 4-column grid showcasing product categories
- **Donate**: Two-column layout with donation info and image placeholder
- **Why Choose**: Feature grid highlighting store benefits
- **Contact**: Form for donation pickup scheduling with contact information
- **Footer**: Multi-column footer with store details

### Form Handling
The contact form in `index.html` (lines 208-232) is currently static HTML with no JavaScript. To make it functional, you'll need to:
1. Add form submission handling (JavaScript or backend endpoint)
2. Implement validation
3. Connect to an email service or database

### Google Ads Compliance
Content is written to avoid problematic keywords that might trigger Google Ads issues, as noted in README.md.

## Customization Points

### Store Information
- Phone numbers and addresses are in the Locations section (lines 48-94 in `index.html`)
- Update store hours in location cards
- Footer also contains duplicate contact info (lines 242-263)

### Branding
- Logo text is in header (line 20 in `index.html`)
- To add a logo image, replace the text `<h1>SuperThrift</h1>` with an `<img>` tag
- Color scheme defined in CSS variables (lines 8-21 in `css/styles.css`)

### Content Updates
All content is in `index.html`. The site uses semantic HTML5 elements and is organized by `<section>` tags with IDs for anchor navigation.
