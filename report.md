# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 16:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 310.5 | 588.9 | 1000ms | 0/218 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.7 | 429.6 | 1500ms | 0/218 |
| ❌ | `nasa_apod` | 78.9% | 60.55% | 2262.4 | 10538.0 | 2000ms | 86/218 |
| ❌ | `ipapi_check` | 94.04% | 100.0% | 155.6 | 252.2 | 2500ms | 0/218 |
| ⚠️ | `open_meteo_weather` | 96.33% | 96.33% | 877.5 | 14877.1 | 2000ms | 8/218 |
| ⚠️ | `dog_ceo_random` | 99.08% | 81.19% | 1293.0 | 5586.8 | 2500ms | 41/218 |
| ✅ | `useless_fact` | 99.08% | 99.54% | 592.4 | 10229.6 | 2500ms | 1/218 |
| ✅ | `catfact_random` | 99.08% | 99.54% | 271.2 | 10070.5 | 3000ms | 1/218 |
| ✅ | `agify_name` | 100.0% | 99.54% | 401.4 | 3237.1 | 2000ms | 1/218 |
| ✅ | `rest_countries` | 100.0% | 98.62% | 294.9 | 7269.1 | 2500ms | 3/218 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.54% | 241.9 | 2314.9 | 2000ms | 1/218 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/218 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |
| `nasa_apod` | 15:00 | 2793.9 | 50.0% |
| `open_meteo_weather` | 05:00 | 2637.8 | 14.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
