# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SuperThrift is a high-conversion, Google Ads optimized landing page for thrift stores in Pearl and Byram, Mississippi. The site is a ministry of Mercy House Adult & Teen Challenge, featuring donation pickup scheduling and store information. Static HTML/CSS with no build process required.

## Deployment

### Cloudflare Pages (Automated)
The site deploys automatically to Cloudflare Pages via GitHub Actions on every push to `main`.

**Setup Requirements:**
1. Add these secrets in GitHub repository settings:
   - `CLOUDFLARE_API_TOKEN` - Create at Cloudflare Dashboard > My Profile > API Tokens
   - `CLOUDFLARE_ACCOUNT_ID` - Found in Cloudflare Dashboard URL or Overview page
2. Create a Cloudflare Pages project named `superthrift`
3. Push to `main` branch to trigger deployment

### Local Development
Open `index.html` directly in a web browser. No build process required.

## Code Architecture

### File Structure
```
superthrift/
├── index.html          # Main landing page (Google Ads optimized)
├── privacy.html        # Privacy policy (required for Google Ads)
├── css/
│   └── styles.css      # Mobile-first CSS with custom properties
├── images/
│   ├── logo.webp       # SuperThrift logo
│   └── superthrift-store.png  # Hero background
├── .github/
│   └── workflows/
│       └── deploy.yml  # Cloudflare Pages deployment
├── IMAGE_TODO.md       # Image requirements checklist
└── CLAUDE.md           # This file
```

### CSS Design System
CSS custom properties in `:root` (lines 10-55 in `css/styles.css`):
- Primary: `--primary` (#dc2626 red) - CTAs, emphasis
- Secondary: `--secondary` (#1d4ed8 blue) - Hero, links
- Success: `--success` (#059669 green) - Checkmarks
- Gold: `--gold` (#d97706) - Stars, accents

### Page Sections (Google Ads Wireframe)
1. **Hero** - Mission statement, 3 benefits, Donate + Shop CTAs
2. **Trust Strip** - Mercy House connection, community message
3. **How It Works** - 3-step visual process
4. **Donation Section** - Items accepted, benefits, pickup CTA
5. **What We Accept** - 6-card grid of donation categories
6. **Shop Section** - Shopping benefits and location CTA
7. **Community Impact** - Mission-focused messaging, stats
8. **Locations** - Pearl and Byram store cards with directions
9. **Social Proof** - Testimonial cards with ratings
10. **Contact Form** - Donation pickup scheduling form
11. **Final CTA** - Strong close with Donate + Shop buttons
12. **Footer** - About, links, locations, privacy policy

### Contact Information
- **Phone:** (601) 768-3532
- **Email:** info@mercyhouseatc.com
- **Pearl:** 434 N Bierdeman Rd, Pearl, MS 39208
- **Byram:** 6787 S Siwell Rd STE D, Byram, MS 39272
- **Hours:** Mon-Sat 8:00 AM - 6:00 PM, Sunday Closed

### Form Handling
The contact form is static HTML. To make it functional:
1. Add a form service (Formspree, Netlify Forms, or custom endpoint)
2. Update the `action` attribute on the form element
3. Add client-side validation if needed

## Google Ads Optimization

### Compliance Checklist
- [x] No addiction, rehab, recovery, treatment language
- [x] Clear business name and purpose stated
- [x] Privacy policy linked in footer
- [x] Contact info visible (phone, email, locations)
- [x] No misleading claims

### Speed Optimization
- Mobile-first CSS
- Minimal dependencies (only Google Fonts)
- No JavaScript required
- Compressed images (use WebP)
- Fast loading sections above the fold

### Keywords Targeted
- thrift store Mississippi
- donate furniture Mississippi
- donate clothes near me
- schedule donation pickup
- Pearl MS / Byram MS thrift

## Customization

### Update Store Info
Edit locations in `index.html`:
- Locations section (lines 240-285)
- Contact section (lines 312-380)
- Footer (lines 395-430)

### Update Colors
Edit CSS custom properties in `css/styles.css` (lines 10-55)

### Add Images
See `IMAGE_TODO.md` for required images and placement instructions.
