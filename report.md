# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 11:17 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.8 | 517.6 | 1000ms | 0/85 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.8 | 234.1 | 1500ms | 0/85 |
| ❌ | `nasa_apod` | 97.65% | 69.41% | 1283.1 | 10538.0 | 2000ms | 26/85 |
| ⚠️ | `open_meteo_weather` | 97.65% | 98.82% | 590.5 | 2550.7 | 2000ms | 1/85 |
| ⚠️ | `ipapi_check` | 97.65% | 100.0% | 153.6 | 248.6 | 2500ms | 0/85 |
| ❌ | `dog_ceo_random` | 100.0% | 74.12% | 1714.2 | 4785.5 | 2500ms | 22/85 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 597.0 | 2439.0 | 2500ms | 0/85 |
| ✅ | `agify_name` | 100.0% | 98.82% | 428.0 | 3237.1 | 2000ms | 1/85 |
| ✅ | `rest_countries` | 100.0% | 98.82% | 283.5 | 5081.4 | 2500ms | 1/85 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 243.9 | 1556.1 | 2000ms | 0/85 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 243.6 | 1218.5 | 3000ms | 0/85 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/85 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `dog_ceo_random` | 13:00 | 2942.8 | 100.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
