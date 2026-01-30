import re
import os

def extract_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract URLs
    urls = re.findall(r'https?://veiltail\.net/wp-content/uploads/20\d\d/\d\d/[^"\' >]+', content)
    unique_urls = sorted(list(set(urls)))
    
    print(f"--- Data from {filepath} ---")
    print(f"Found {len(unique_urls)} unique upload URLs.")
    for url in unique_urls:
        if any(ext in url.lower() for ext in ['.jpg', '.png', '.jpeg', '.svg', '.webp']):
            print(f"IMAGE: {url}")

    # Extract team names (approximation)
    # Looking for <h3>Name</h3> followed by images or vice versa
    team_members = re.findall(r'<h3>([^<]+)</h3>', content)
    print("\nPotential Team/Items:")
    for item in team_members:
        print(f"ITEM: {item}")

    # Extract testimonials (approximation)
    # Looking for Dar Gozour or specific Arabic phrases
    testimonials = re.findall(r'<div class="testimonial-content">.*?<p>(.*?)</p>.*?<div class="testimonial-name">(.*?)</div>', content, re.DOTALL)
    print("\nPotential Testimonials:")
    for text, name in testimonials:
        print(f"TESTIMONIAL by {name}: {text[:100]}...")

if __name__ == "__main__":
    extract_data(r"d:\veiltail training\veil-feat-static-veiltail-site\about-us-raw.html")
    extract_data(r"d:\veiltail training\veil-feat-static-veiltail-site\our-work-raw.html")
