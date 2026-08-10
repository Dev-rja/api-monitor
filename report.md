# API Reliability Monitor — SLA Report

> Last updated: **2026-08-10 08:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.87% | 2853.0 | 10420.1 | 1000ms | 497/1832 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 132.1 | 5052.3 | 1500ms | 7/1832 |
| ❌ | `ipapi_check` | 63.97% | 99.95% | 148.2 | 4507.0 | 2500ms | 1/1832 |
| ❌ | `nasa_apod` | 77.18% | 53.66% | 3056.6 | 11152.5 | 2000ms | 849/1832 |
| ⚠️ | `dog_ceo_random` | 95.85% | 96.89% | 527.9 | 10244.1 | 2500ms | 57/1832 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.76% | 692.4 | 14877.1 | 2000ms | 41/1832 |
| ✅ | `rest_countries` | 99.18% | 98.85% | 289.2 | 10221.5 | 2500ms | 21/1832 |
| ✅ | `useless_fact` | 99.73% | 99.62% | 649.6 | 10229.6 | 2500ms | 7/1832 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.95% | 96.9 | 4328.4 | 1500ms | 1/1832 |
| ✅ | `catfact_random` | 99.84% | 99.45% | 258.2 | 10080.2 | 3000ms | 10/1832 |
| ✅ | `agify_name` | 99.89% | 99.73% | 391.4 | 16112.2 | 2000ms | 5/1832 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 196.3 | 3882.8 | 2000ms | 2/1832 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5124.8 | 70.0% |
| `numbers_trivia` | 03:00 | 4867.8 | 48.65% |
| `nasa_apod` | 05:00 | 4572.2 | 62.79% |
| `nasa_apod` | 03:00 | 4105.3 | 62.16% |
| `nasa_apod` | 17:00 | 3760.8 | 50.54% |
| `numbers_trivia` | 10:00 | 3732.7 | 35.29% |
| `nasa_apod` | 09:00 | 3707.4 | 50.67% |
| `nasa_apod` | 11:00 | 3605.8 | 51.0% |
| `numbers_trivia` | 14:00 | 3528.9 | 34.15% |
| `nasa_apod` | 01:00 | 3333.4 | 48.21% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
