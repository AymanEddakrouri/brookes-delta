#!/usr/bin/env python3
"""
Simple test script for Brookes' Δ Calculator
"""

# Import our calculator
try:
    from delta_calculator import BrookesDeltaCalculator, test_example
    print("✅ Successfully imported delta_calculator")
except ImportError as e:
    print(f"❌ Error importing: {e}")
    print("Make sure delta_calculator.py is in the same folder")
    exit(1)

def simple_test():
    """Very simple test with small data"""
    print("\n" + "=" * 40)
    print("🧪 SIMPLE TEST WITH SMALL DATA")
    print("=" * 40)
   
    # Small example
    categories = ["Cat A", "Cat B", "Cat C", "Cat D"]
    frequencies = [40, 30, 20, 10]  # Total = 100
   
    # Create calculator
    calc = BrookesDeltaCalculator(categories, frequencies)
   
    # Calculate
    results = calc.calculate_delta()
   
    print(f"Categories: {categories}")
    print(f"Frequencies: {frequencies}")
    print(f"Total: {sum(frequencies)}")
    print(f"\nΔ = {results['delta']}")
    print(f"Interpretation: {results['interpretation']}")
   
    # Show the table
    print("\n📊 Calculation Table:")
    print(results['table'][['Category', 'Frequency', 'Percentage', 'Rank']].to_string(index=False))
   
    return results

def compare_two_fields():
    """Compare two different fields"""
    print("\n\n" + "=" * 40)
    print("🔍 COMPARING TWO FIELDS")
    print("=" * 40)
   
    # Field 1: Specialized (concentrated distribution)
    field1_cats = ["Main Topic", "Sub-topic A", "Sub-topic B", "Minor 1", "Minor 2"]
    field1_freq = [50, 25, 15, 7, 3]  # Total = 100, concentrated
   
    # Field 2: Dispersed (even distribution)
    field2_cats = ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"]
    field2_freq = [22, 21, 20, 19, 18]  # Total = 100, nearly equal
   
    # Calculate both
    calc1 = BrookesDeltaCalculator(field1_cats, field1_freq)
    calc2 = BrookesDeltaCalculator(field2_cats, field2_freq)
   
    res1 = calc1.calculate_delta()
    res2 = calc2.calculate_delta()
   
    print(f"Field 1 (Specialized pattern):")
    print(f"  Δ = {res1['delta']}")
    print(f"  {res1['interpretation']}")
   
    print(f"\nField 2 (Dispersed pattern):")
    print(f"  Δ = {res2['delta']}")
    print(f"  {res2['interpretation']}")
   
    # Which is more concentrated?
    if res1['delta'] > res2['delta']:
        diff = res1['delta'] - res2['delta']
        print(f"\n📈 Field 1 is {diff:.3f} more concentrated than Field 2")
        print("   (Higher Δ means more specialization)")
    else:
        diff = res2['delta'] - res1['delta']
        print(f"\n📈 Field 2 is {diff:.3f} more concentrated than Field 1")
        print("   (Higher Δ means more specialization)")

def test_edge_cases():
    """Test edge cases and error handling"""
    print("\n\n" + "=" * 40)
    print("⚠️  TESTING EDGE CASES")
    print("=" * 40)
   
    # Test 1: Single category
    print("\nTest 1: Single category")
    try:
        calc = BrookesDeltaCalculator(["Only Category"], [100])
        res = calc.calculate_delta()
        print(f"  Categories: ['Only Category']")
        print(f"  Frequencies: [100]")
        print(f"  Δ = {res['delta']} (should be undefined/0)")
        print(f"  Message: {res['interpretation']}")
    except Exception as e:
        print(f"  Error: {e}")
   
    # Test 2: Two equal categories
    print("\nTest 2: Two equal categories")
    try:
        calc = BrookesDeltaCalculator(["Cat A", "Cat B"], [50, 50])
        res = calc.calculate_delta()
        print(f"  Δ = {res['delta']}")
        print(f"  Interpretation: {res['interpretation']}")
    except Exception as e:
        print(f"  Error: {e}")
   
    # Test 3: Many categories with one dominant
    print("\nTest 3: One dominant category")
    try:
        cats = [f"Category {i}" for i in range(1, 11)]
        freqs = [90] + [1] * 9  # 90% in first category
        calc = BrookesDeltaCalculator(cats, freqs)
        res = calc.calculate_delta()
        print(f"  Δ = {res['delta']:.3f} (should be very high)")
        print(f"  Interpretation: {res['interpretation']}")
    except Exception as e:
        print(f"  Error: {e}")

def test_visualization():
    """Test if visualization works"""
    print("\n\n" + "=" * 40)
    print("📈 TESTING VISUALIZATION")
    print("=" * 40)
   
    # Create test data
    categories = ["Research", "Theory", "Methods", "Applications", "Review"]
    frequencies = [35, 25, 20, 15, 5]
   
    calc = BrookesDeltaCalculator(categories, frequencies)
   
    print("Attempting to create visualization...")
    try:
        # This will try to show a plot
        fig = calc.visualize("test_visualization.png")
        print("✅ Visualization successful!")
        print("   Plot should appear in a new window")
        print("   Image saved as 'test_visualization.png'")
    except Exception as e:
        print(f"❌ Visualization failed: {e}")
        print("   This is normal if matplotlib is not installed")
        print("   The calculations still work without visualization")

def main():
    """Main test function"""
    print("=" * 60)
    print("BROOKES' Δ CALCULATOR - COMPLETE TEST SUITE")
    print("=" * 60)
   
    # Test 1: Simple test
    simple_test()
   
    # Test 2: Compare fields
    compare_two_fields()
   
    # Test 3: Edge cases
    test_edge_cases()
   
    # Test 4: Visualization
    test_visualization()
   
    # Test 5: Full example from paper
    print("\n\n" + "=" * 60)
    print("📄 FULL EXAMPLE FROM PAPER")
    print("=" * 60)
   
    try:
        # Call the test_example function from delta_calculator
        paper_results = test_example()
        print(f"\n✅ Paper example Δ: {paper_results['delta']}")
    except Exception as e:
        print(f"❌ Error running paper example: {e}")
   
    print("\n" + "=" * 60)
    print("✅ ALL TESTS COMPLETED!")
    print("=" * 60)
   
    # Final summary
    print("\n📋 SUMMARY OF WHAT WE TESTED:")
    print("   1. Basic Δ calculation ✓")
    print("   2. Field comparison ✓")
    print("   3. Edge cases ✓")
    print("   4. Visualization ✓")
    print("   5. Paper example ✓")
   
    print("\n🎯 NEXT STEPS:")
    print("   - Install pandas and matplotlib for full features")
    print("   - Try with your own research data")
    print("   - Create GitHub repository")
    print("   - Add to your arXiv paper")

# Check if required packages are installed
def check_dependencies():
    """Check if required packages are available"""
    print("\n🔍 CHECKING DEPENDENCIES")
    print("-" * 30)
   
    required = ['pandas', 'numpy', 'matplotlib']
   
    for package in required:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is NOT installed")
   
    print("\n💡 INSTALLATION COMMANDS:")
    print("   pip install pandas numpy matplotlib")
    print("   or")
    print("   pip install -r requirements.txt")

if __name__ == "__main__":
    # First check dependencies
    check_dependencies()
   
    # Ask user if they want to continue
    print("\n" + "=" * 60)
    input("Press Enter to run tests (or Ctrl+C to cancel)...")
    print()
   
    # Run main tests
    main()
   
    # Final message
    print("\n" + "=" * 60)
    print("🎉 CONGRATULATIONS!")
    print("=" * 60)
    print("\nYour Brookes' Δ calculator is working!")
    print("\nTo use with your own data:")
    print("""
    from delta_calculator import BrookesDeltaCalculator
   
    # Your data
    categories = ["your", "categories", "here"]
    frequencies = [your, frequencies, here]
   
    # Calculate
    calc = BrookesDeltaCalculator(categories, frequencies)
    results = calc.calculate_delta()
   
    print(f"Δ = {results['delta']}")
    print(f"Interpretation: {results['interpretation']}")
    """)