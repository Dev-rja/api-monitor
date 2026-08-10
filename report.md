# API Reliability Monitor — SLA Report

> Last updated: **2026-08-10 01:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.03% | 2837.2 | 10420.1 | 1000ms | 493/1828 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 130.9 | 5052.3 | 1500ms | 6/1828 |
| ❌ | `ipapi_check` | 64.11% | 99.95% | 148.3 | 4507.0 | 2500ms | 1/1828 |
| ❌ | `nasa_apod` | 77.35% | 53.77% | 3040.8 | 11152.5 | 2000ms | 845/1828 |
| ⚠️ | `dog_ceo_random` | 95.84% | 96.88% | 528.4 | 10244.1 | 2500ms | 57/1828 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.76% | 692.6 | 14877.1 | 2000ms | 41/1828 |
| ✅ | `rest_countries` | 99.18% | 98.85% | 289.3 | 10221.5 | 2500ms | 21/1828 |
| ✅ | `useless_fact` | 99.73% | 99.62% | 649.6 | 10229.6 | 2500ms | 7/1828 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.95% | 96.9 | 4328.4 | 1500ms | 1/1828 |
| ✅ | `catfact_random` | 99.84% | 99.45% | 258.1 | 10080.2 | 3000ms | 10/1828 |
| ✅ | `agify_name` | 99.89% | 99.73% | 391.6 | 16112.2 | 2000ms | 5/1828 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 196.5 | 3882.8 | 2000ms | 2/1828 |

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
| `nasa_apod` | 01:00 | 3333.4 | 48.21% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
