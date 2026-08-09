# API Reliability Monitor — SLA Report

> Last updated: **2026-08-09 04:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.21% | 2720.4 | 10420.1 | 1000ms | 464/1799 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 131.1 | 5052.3 | 1500ms | 6/1799 |
| ❌ | `ipapi_check` | 64.92% | 99.94% | 148.9 | 4507.0 | 2500ms | 1/1799 |
| ❌ | `nasa_apod` | 77.54% | 54.53% | 3011.9 | 11152.5 | 2000ms | 818/1799 |
| ⚠️ | `dog_ceo_random` | 95.78% | 96.83% | 531.1 | 10244.1 | 2500ms | 57/1799 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.72% | 693.0 | 14877.1 | 2000ms | 41/1799 |
| ✅ | `rest_countries` | 99.17% | 98.83% | 291.0 | 10221.5 | 2500ms | 21/1799 |
| ✅ | `useless_fact` | 99.72% | 99.61% | 649.4 | 10229.6 | 2500ms | 7/1799 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.94% | 97.1 | 4328.4 | 1500ms | 1/1799 |
| ✅ | `catfact_random` | 99.83% | 99.44% | 258.4 | 10080.2 | 3000ms | 10/1799 |
| ✅ | `agify_name` | 99.89% | 99.72% | 390.8 | 16112.2 | 2000ms | 5/1799 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 197.4 | 3882.8 | 2000ms | 2/1799 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5124.8 | 70.0% |
| `numbers_trivia` | 03:00 | 4723.8 | 47.22% |
| `nasa_apod` | 05:00 | 4505.5 | 61.9% |
| `nasa_apod` | 03:00 | 3937.9 | 61.11% |
| `nasa_apod` | 09:00 | 3740.6 | 49.32% |
| `nasa_apod` | 17:00 | 3728.4 | 50.55% |
| `numbers_trivia` | 10:00 | 3638.5 | 34.33% |
| `nasa_apod` | 11:00 | 3547.5 | 50.0% |
| `numbers_trivia` | 14:00 | 3365.7 | 32.5% |
| `nasa_apod` | 01:00 | 3347.6 | 47.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
