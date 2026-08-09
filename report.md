# API Reliability Monitor — SLA Report

> Last updated: **2026-08-09 11:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.88% | 2753.0 | 10420.1 | 1000ms | 472/1807 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 131.0 | 5052.3 | 1500ms | 6/1807 |
| ❌ | `ipapi_check` | 64.69% | 99.94% | 148.7 | 4507.0 | 2500ms | 1/1807 |
| ❌ | `nasa_apod` | 77.53% | 54.29% | 3021.1 | 11152.5 | 2000ms | 826/1807 |
| ⚠️ | `dog_ceo_random` | 95.79% | 96.85% | 530.2 | 10244.1 | 2500ms | 57/1807 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.73% | 693.2 | 14877.1 | 2000ms | 41/1807 |
| ✅ | `rest_countries` | 99.17% | 98.84% | 290.4 | 10221.5 | 2500ms | 21/1807 |
| ✅ | `useless_fact` | 99.72% | 99.61% | 649.2 | 10229.6 | 2500ms | 7/1807 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.94% | 97.0 | 4328.4 | 1500ms | 1/1807 |
| ✅ | `catfact_random` | 99.83% | 99.45% | 257.8 | 10080.2 | 3000ms | 10/1807 |
| ✅ | `agify_name` | 99.89% | 99.72% | 391.0 | 16112.2 | 2000ms | 5/1807 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 197.1 | 3882.8 | 2000ms | 2/1807 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5124.8 | 70.0% |
| `numbers_trivia` | 03:00 | 4723.8 | 47.22% |
| `nasa_apod` | 05:00 | 4572.2 | 62.79% |
| `nasa_apod` | 03:00 | 3937.9 | 61.11% |
| `numbers_trivia` | 10:00 | 3732.7 | 35.29% |
| `nasa_apod` | 17:00 | 3728.4 | 50.55% |
| `nasa_apod` | 09:00 | 3707.4 | 50.67% |
| `nasa_apod` | 11:00 | 3615.3 | 50.51% |
| `numbers_trivia` | 14:00 | 3365.7 | 32.5% |
| `nasa_apod` | 01:00 | 3347.6 | 47.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
