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
├── README.md           # Project overview and setup instructions
├── CLAUDE.md           # This file - development guide
├── css/
│   └── styles.css      # Mobile-first CSS with custom properties
├── images/
│   ├── logo.webp                           # SuperThrift header logo
│   ├── superthrift-store.png               # Hero background image
│   ├── donation-photo.webp                 # Donation section (above-fold)
│   ├── store-interior.webp                 # Shop section (below-fold)
│   ├── community-impact-pearl-brandon.png  # Community impact section (below-fold)
│   ├── superthrift_full_logo_red_512x512.png  # Full color logo variant
│   ├── hero2.png                           # Alternative hero image
│   ├── donor-pickup.png                    # Donation pickup imagery
│   └── store-interior.jpeg                 # Store interior JPEG version
└── .github/
    └── workflows/
        └── deploy.yml  # Cloudflare Pages deployment
```

### CSS Design System
CSS custom properties in `:root` (lines 10-55 in `css/styles.css`):
- Primary: `--primary` (#dc2626 red) - CTAs, emphasis
- Secondary: `--secondary` (#1d4ed8 blue) - Hero, links
- Success: `--success` (#059669 green) - Checkmarks
- Gold: `--gold` (#d97706) - Stars, accents

### Page Sections (Google Ads Wireframe)
1. **Hero** - Mission statement, 3 benefits, Donate + Shop CTAs (with gradient overlay for text readability)
2. **Trust Strip** - Mercy House connection, community message
3. **How It Works** - 3-step visual process
4. **Donation Section** - Items accepted, benefits, pickup CTA (with donation-photo.webp)
5. **What We Accept** - 6-card grid of donation categories
6. **Shop Section** - Shopping benefits and location CTA (with store-interior.webp)
7. **Community Impact** - Mission-focused messaging, stats (with community-impact-pearl-brandon.png)
8. **Locations** - Pearl and Byram store cards with directions
9. **Social Proof** - Testimonial cards with ratings
10. **Contact Form** - Donation pickup scheduling form
11. **Final CTA** - Strong close with Donate + Shop buttons
12. **Footer** - About, links, locations, privacy policy, 501(c)(3) GuideStar Platinum badge

### Contact Information
- **Phone:** (601) 768-3532
- **Email:** info@mercyhouseatc.com
- **Pearl:** 434 N Bierdeman Rd, Pearl, MS 39208
- **Byram:** 6787 S Siwell Rd STE D, Byram, MS 39272
- **Hours:** Mon-Sat 8:00 AM - 6:00 PM, Sunday Closed

### Form Handling
The donation pickup form is integrated with Formspree:
- **Primary Form**: Full donation pickup form in contact section
  - Action: `https://formspree.io/f/xzdekbzd`
  - Fields: Name, Phone, Email, Pickup Address, Preferred Location, Items
  - Hidden field: `_subject` for email subject customization
- **Popup Widget**: Formbutton widget (floating button in bottom-right)
  - Quick contact option for users
  - Same Formspree endpoint
  - Custom styling with brand colors (#dc2626 red)
  - Fields: Name, Email, Phone, Message

## Google Ads Optimization

### Compliance Checklist
- [x] No addiction, rehab, recovery, treatment language
- [x] Clear business name and purpose stated
- [x] Privacy policy linked in footer
- [x] Contact info visible (phone, email, locations)
- [x] No misleading claims

### Speed Optimization
- **LCP Optimization**: Hero image and logo preloaded with `fetchpriority="high"`
- **Resource Hints**: Critical images discoverable from HTML immediately
- **Lazy Loading**: Below-fold images use `loading="lazy"` attribute
- **Mobile-first CSS**: Optimized for mobile performance first
- **Minimal Dependencies**: Only Google Fonts, no JavaScript frameworks
- **Image Formats**: WebP for smaller file sizes where possible
- **Critical Request Chain**: Preload directives reduce render-blocking resources

### Keywords Targeted
- thrift store Mississippi
- donate furniture Mississippi
- donate clothes near me
- schedule donation pickup
- Pearl MS / Byram MS thrift

## Visual Design

### Hero Section Gradient Overlay
To ensure white text remains readable on the hero background, a dual-color gradient overlay is applied:
- Gradient: Blue (#1e40af at 85% opacity) to Red (#dc2626 at 85% opacity)
- Direction: 135deg diagonal
- Text shadow: 2px 2px 4px rgba(0,0,0,0.3) for additional contrast
- Location: `.hero-bg::after` pseudo-element in `css/styles.css`

### 501(c)(3) Nonprofit Badge
GuideStar Platinum Seal of Transparency is displayed in the footer:
- **Organization**: Mercy House Teen Challenge (EIN: 45-4670832)
- **Badge Type**: Platinum Seal of Transparency
- **Link**: https://app.candid.org/profile/9237605/
- **Image**: SVG hosted by GuideStar widgets
- **Location**: Footer section with hover animation

### Performance Optimizations
**Above-the-fold Images (High Priority):**
- Hero background: Preloaded with `fetchpriority="high"`
- Logo: Preloaded with `fetchpriority="high"`
- Donation photo: `fetchpriority="high"` attribute

**Below-the-fold Images (Lazy Loaded):**
- Community impact photo: `loading="lazy"`
- Store interior photo: `loading="lazy"`

## Customization

### Update Store Info
Edit locations in `index.html`:
- Locations section (around lines 240-285)
- Contact section (around lines 312-380)
- Footer (around lines 395-430)

### Update Colors
Edit CSS custom properties in `css/styles.css` (lines 10-55)

### Update Images
All placeholder images have been replaced with actual photography:
- ✅ Hero background: `superthrift-store (2).png` (needs file correction)
- ✅ Logo: `logo.webp`
- ✅ Donation section: `donation-photo.webp`
- ✅ Shop section: `store-interior.webp`
- ✅ Community impact: `community-impact-pearl-brandon.png`

**Note**: The hero image reference in `index.html` points to `superthrift-store (2).png` but the file doesn't exist. Either rename the existing file or update the HTML reference.
