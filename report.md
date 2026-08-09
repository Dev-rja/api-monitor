# API Reliability Monitor — SLA Report

> Last updated: **2026-08-09 18:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.43% | 2797.3 | 10420.1 | 1000ms | 483/1818 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 131.1 | 5052.3 | 1500ms | 6/1818 |
| ❌ | `ipapi_check` | 64.36% | 99.94% | 148.4 | 4507.0 | 2500ms | 1/1818 |
| ❌ | `nasa_apod` | 77.39% | 54.07% | 3032.6 | 11152.5 | 2000ms | 835/1818 |
| ⚠️ | `dog_ceo_random` | 95.82% | 96.86% | 529.2 | 10244.1 | 2500ms | 57/1818 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.74% | 692.9 | 14877.1 | 2000ms | 41/1818 |
| ✅ | `rest_countries` | 99.17% | 98.84% | 289.9 | 10221.5 | 2500ms | 21/1818 |
| ✅ | `useless_fact` | 99.72% | 99.61% | 649.4 | 10229.6 | 2500ms | 7/1818 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.94% | 97.0 | 4328.4 | 1500ms | 1/1818 |
| ✅ | `catfact_random` | 99.83% | 99.45% | 257.6 | 10080.2 | 3000ms | 10/1818 |
| ✅ | `agify_name` | 99.89% | 99.72% | 391.2 | 16112.2 | 2000ms | 5/1818 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 196.8 | 3882.8 | 2000ms | 2/1818 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5124.8 | 70.0% |
| `numbers_trivia` | 03:00 | 4723.8 | 47.22% |
| `nasa_apod` | 05:00 | 4572.2 | 62.79% |
| `nasa_apod` | 03:00 | 3937.9 | 61.11% |
| `nasa_apod` | 17:00 | 3760.8 | 50.54% |
| `numbers_trivia` | 10:00 | 3732.7 | 35.29% |
| `nasa_apod` | 09:00 | 3707.4 | 50.67% |
| `nasa_apod` | 11:00 | 3605.8 | 51.0% |
| `numbers_trivia` | 14:00 | 3528.9 | 34.15% |
| `nasa_apod` | 01:00 | 3347.6 | 47.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
