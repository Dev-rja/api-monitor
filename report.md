# API Reliability Monitor — SLA Report

> Last updated: **2026-04-05 13:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **82.8%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 302.7 | 517.6 | 1000ms | 0/88 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 116.5 | 234.1 | 1500ms | 0/88 |
| ❌ | `nasa_apod` | 97.73% | 68.18% | 1303.1 | 10538.0 | 2000ms | 28/88 |
| ⚠️ | `open_meteo_weather` | 97.73% | 98.86% | 587.8 | 2550.7 | 2000ms | 1/88 |
| ⚠️ | `ipapi_check` | 97.73% | 100.0% | 154.7 | 248.6 | 2500ms | 0/88 |
| ❌ | `dog_ceo_random` | 100.0% | 72.73% | 1774.9 | 5142.0 | 2500ms | 24/88 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 595.6 | 2439.0 | 2500ms | 0/88 |
| ✅ | `agify_name` | 100.0% | 98.86% | 420.9 | 3237.1 | 2000ms | 1/88 |
| ✅ | `rest_countries` | 100.0% | 98.86% | 278.8 | 5081.4 | 2500ms | 1/88 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 243.2 | 1556.1 | 2000ms | 0/88 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 242.7 | 1218.5 | 3000ms | 0/88 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.5 | 252.0 | 1500ms | 0/88 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 13:00 | 3675.8 | 100.0% |
| `dog_ceo_random` | 17:00 | 3292.2 | 80.0% |
| `dog_ceo_random` | 03:00 | 3274.4 | 100.0% |
| `dog_ceo_random` | 14:00 | 3011.8 | 75.0% |
| `nasa_apod` | 10:00 | 2892.2 | 25.0% |
| `nasa_apod` | 03:00 | 2530.9 | 100.0% |
| `nasa_apod` | 22:00 | 2191.3 | 16.67% |
| `nasa_apod` | 07:00 | 2071.8 | 75.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
