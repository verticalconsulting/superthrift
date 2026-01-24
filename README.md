# SuperThrift Landing Page

A high-conversion, Google Ads optimized landing page for SuperThrift thrift stores in Pearl and Byram, Mississippi. SuperThrift is a ministry of Mercy House Adult & Teen Challenge, a 501(c)(3) nonprofit organization.

## Overview

This static HTML/CSS website features:
- **Two Store Locations**: Pearl and Byram, Mississippi
- **Donation Pickup Scheduling**: Free pickup service with tax receipt
- **501(c)(3) Verification**: GuideStar Platinum Seal of Transparency
- **Mobile-First Design**: Optimized for all devices
- **Performance Optimized**: LCP optimization with resource hints and lazy loading
- **Google Ads Compliant**: Content carefully crafted to meet advertising guidelines

## Key Features

### Performance & SEO
- **LCP Optimized**: Hero image and logo preloaded with `fetchpriority="high"`
- **Lazy Loading**: Below-fold images load on demand
- **Mobile-First CSS**: Optimized for mobile performance
- **No JavaScript Required**: Pure HTML/CSS for maximum speed
- **Google Ads Compliant**: No addiction/treatment language

### Design & UX
- **Gradient Overlay Hero**: Blue-to-red gradient ensures text readability
- **Responsive Design**: Perfect on all devices
- **Visual Hierarchy**: 12 strategically ordered sections
- **Trust Elements**: 501(c)(3) badge, testimonials, community impact

### Functionality
- **Contact Form**: Donation pickup scheduling powered by Formspree
  - Full form in contact section with pickup details
  - Floating popup widget for quick contact
- **Two Locations**: Pearl (434 N Bierdeman Rd) and Byram (6787 S Siwell Rd)
- **Store Hours**: Mon-Sat 8:00 AM - 6:00 PM, Sunday Closed
- **Phone**: (601) 768-3532
- **Email**: info@mercyhouseatc.com

## Getting Started

### Local Development

1. Clone this repository
2. Open `index.html` in your web browser
3. No build process required - it's a static HTML site!

### Deployment

**Automated Cloudflare Pages Deployment** (Recommended):
This site deploys automatically via GitHub Actions on every push to `main`.

**Setup Steps:**
1. Add these secrets in GitHub repository settings:
   - `CLOUDFLARE_API_TOKEN` - Create at Cloudflare Dashboard > My Profile > API Tokens
   - `CLOUDFLARE_ACCOUNT_ID` - Found in Cloudflare Dashboard URL or Overview page
2. Create a Cloudflare Pages project named `superthrift`
3. Push to `main` branch to trigger deployment

**Alternative Options:**
- GitHub Pages
- Netlify
- Vercel
- Traditional web hosting (upload via FTP)

### Customization

To customize the site:

1. **Update Contact Information**: Edit phone, email, addresses in `index.html`
2. **Change Colors**: Modify CSS custom properties in `css/styles.css` (lines 10-55)
3. **Replace Images**: See image references in CLAUDE.md
4. **Update Hours**: Modify store hours in locations section
5. **Form Configuration**: Update Formspree endpoint in form action and Formbutton script

## File Structure

```
superthrift/
├── index.html          # Main landing page (Google Ads optimized)
├── privacy.html        # Privacy policy (required for Google Ads)
├── README.md           # This file - project overview
├── CLAUDE.md           # Development guide for Claude Code
├── css/
│   └── styles.css      # Mobile-first CSS with custom properties
├── images/
│   ├── logo.webp                           # SuperThrift header logo
│   ├── superthrift-store.png               # Hero background image
│   ├── donation-photo.webp                 # Donation section (above-fold)
│   ├── store-interior.webp                 # Shop section (below-fold)
│   ├── community-impact-pearl-brandon.png  # Community impact (below-fold)
│   ├── superthrift_full_logo_red_512x512.png  # Full color logo
│   ├── hero2.png                           # Alternative hero image
│   ├── donor-pickup.png                    # Donation pickup imagery
│   └── store-interior.jpeg                 # Store interior JPEG
└── .github/
    └── workflows/
        └── deploy.yml  # Cloudflare Pages deployment automation
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

See LICENSE file for details.

## Technical Details

### CSS Design System
- **Primary**: `#dc2626` (red) - CTAs, emphasis
- **Secondary**: `#1d4ed8` (blue) - Hero, links
- **Success**: `#059669` (green) - Checkmarks
- **Gold**: `#d97706` (yellow) - Stars, accents

### Performance Optimizations
- Hero background and logo preloaded with `fetchpriority="high"`
- Below-fold images use `loading="lazy"`
- WebP image format for smaller file sizes
- No JavaScript frameworks
- Gradient overlay for hero text readability

### Google Ads Compliance
- ✅ No addiction, rehab, recovery, treatment language
- ✅ Privacy policy linked in footer
- ✅ Contact information visible
- ✅ 501(c)(3) verification displayed
- ✅ No misleading claims

## Contact

**SuperThrift Locations:**
- **Pearl**: 434 N Bierdeman Rd, Pearl, MS 39208
- **Byram**: 6787 S Siwell Rd STE D, Byram, MS 39272
- **Phone**: (601) 768-3532
- **Email**: info@mercyhouseatc.com
- **Hours**: Mon-Sat 8:00 AM - 6:00 PM, Sunday Closed

**Mercy House Adult & Teen Challenge:**
- 501(c)(3) Nonprofit Organization
- EIN: 45-4670832
- GuideStar Platinum Seal of Transparency