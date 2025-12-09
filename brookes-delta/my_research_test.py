#!/usr/bin/env python3
"""
Test Brookes' Δ with YOUR research data
"""

from delta_calculator import BrookesDeltaCalculator

print("=" * 60)
print("BROOKES' Δ FOR YOUR RESEARCH")
print("=" * 60)

# ============================================
# EXAMPLE 1: Test with Effat University data
# ============================================
print("\n📚 EXAMPLE 1: Library Science Subfields")
print("-" * 40)

# Modify these with YOUR actual data!
library_categories = [
    "Digital Libraries",
    "Information Retrieval",
    "Cataloging & Metadata",
    "Information Literacy",
    "Archival Science",
    "Knowledge Management"
]

# These are EXAMPLE frequencies - replace with YOUR data
library_frequencies = [45, 38, 28, 22, 15, 12]  # Total = 160

# Create calculator
lib_calc = BrookesDeltaCalculator(library_categories, library_frequencies)
lib_results = lib_calc.calculate_delta()

print(f"Categories: {library_categories}")
print(f"Frequencies: {library_frequencies}")
print(f"Total publications: {lib_results['total_publications']}")
print(f"Number of categories: {lib_results['T']}")
print(f"\n📊 RESULTS:")
print(f"  Brookes' Δ = {lib_results['delta']}")
print(f"  Interpretation: {lib_results['interpretation']}")

# Show the table
print("\n📋 Detailed Calculation:")
print(lib_results['table'][['Category', 'Frequency', 'Percentage', 'Rank']].to_string(index=False))

# ============================================
# EXAMPLE 2: Compare two journals
# ============================================
print("\n\n📖 EXAMPLE 2: Comparing Two Academic Journals")
print("-" * 40)

# Journal A (Specialized)
journal_a_cats = ["Topic A", "Topic B", "Topic C", "Topic D", "Topic E"]
journal_a_freq = [65, 20, 10, 3, 2]  # Concentrated

# Journal B (General)
journal_b_cats = ["Topic A", "Topic B", "Topic C", "Topic D", "Topic E"]
journal_b_freq = [25, 23, 22, 18, 12]  # More even

# Calculate
calc_a = BrookesDeltaCalculator(journal_a_cats, journal_a_freq)
calc_b = BrookesDeltaCalculator(journal_b_cats, journal_b_freq)

res_a = calc_a.calculate_delta()
res_b = calc_b.calculate_delta()

print("Journal A (Specialized):")
print(f"  Δ = {res_a['delta']} - {res_a['interpretation']}")

print("\nJournal B (General):")
print(f"  Δ = {res_b['delta']} - {res_b['interpretation']}")

# Comparison
comparison = calc_a.compare_fields(calc_b)
print(f"\n🔍 Comparison: {comparison['comparison']}")
print(f"   Δ difference: {comparison['difference']:.3f}")

# ============================================
# EXAMPLE 3: Your actual research data
# ============================================
print("\n\n🎯 EXAMPLE 3: YOUR ACTUAL RESEARCH DATA")
print("-" * 40)
print("Replace the values below with YOUR actual data!")

# DELETE THESE EXAMPLE VALUES AND ADD YOURS!
your_categories = [
    "Arabic Literature & AI",
    "Digital Humanities",
    "Computational Linguistics",
    "Bibliometrics",
    "Other"
]

your_frequencies = [30, 25, 20, 15, 10]  # REPLACE WITH YOUR ACTUAL COUNTS!

your_calc = BrookesDeltaCalculator(your_categories, your_frequencies)
your_results = your_calc.calculate_delta()

print(f"\nYOUR RESEARCH ANALYSIS:")
print(f"Δ = {your_results['delta']}")
print(f"Interpretation: {your_results['interpretation']}")

if your_results['delta'] > 0.6:
    print("→ Your research shows thematic concentration (specialization)")
elif your_results['delta'] < 0.4:
    print("→ Your research shows thematic dispersion (interdisciplinarity)")
else:
    print("→ Your research shows balanced thematic distribution")

print("\n" + "=" * 60)
print("✅ ANALYSIS COMPLETE")
print("=" * 60)
print("\n💡 TIP: Save this output for your arXiv paper!")
print("   Include the Δ value and interpretation in your results section.")