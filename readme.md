# Vertigo Games – Data Analyst Case Study

## Objective
Evaluate two difficulty-flow variants using cohort-based modeling to determine:
- DAU evolution
- Revenue performance
- Impact of temporary and permanent interventions

---

## Methodology
- Daily cohort simulation (20,000 installs/day)
- Log-linear retention interpolation
- Constant ARPPU across variants
- Revenue = IAP + Ads
- No randomness (fully deterministic)

---

## Key Findings

### DAU
- Variant A performs better in early days
- Variant B retains significantly more users after Day 14
- By Day 15 and beyond, Variant B has higher DAU

### Revenue
| Horizon | Winner |
|------|------|
| Day 15 | A (slight) |
| Day 30 | **B (clear)** |

### Sale Scenario (Day 15–25)
- Sale boosts both variants
- Variant B benefits more due to higher DAU
- Winner unchanged

### New User Source (Permanent)
- Variant B decay rate is significantly lower
- Long-term revenue gap increases further

---

## Final Recommendation

**Winner Variant: B**

If only one improvement can be prioritized:
- ❌ Temporary sale
- ✅ Permanent new user source

Long-term retention and monetization efficiency dominate short-term uplifts.

---

## Release
Final version tagged as **v1.0**
