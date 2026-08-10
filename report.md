# API Reliability Monitor — SLA Report

> Last updated: **2026-08-10 11:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.75% | 2864.7 | 10420.1 | 1000ms | 500/1835 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 132.0 | 5052.3 | 1500ms | 7/1835 |
| ❌ | `ipapi_check` | 63.87% | 99.95% | 148.1 | 4507.0 | 2500ms | 1/1835 |
| ❌ | `nasa_apod` | 77.11% | 53.57% | 3064.8 | 11152.5 | 2000ms | 852/1835 |
| ⚠️ | `dog_ceo_random` | 95.86% | 96.89% | 527.7 | 10244.1 | 2500ms | 57/1835 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.77% | 692.1 | 14877.1 | 2000ms | 41/1835 |
| ✅ | `rest_countries` | 99.18% | 98.86% | 288.9 | 10221.5 | 2500ms | 21/1835 |
| ✅ | `useless_fact` | 99.73% | 99.62% | 649.8 | 10229.6 | 2500ms | 7/1835 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.95% | 96.8 | 4328.4 | 1500ms | 1/1835 |
| ✅ | `catfact_random` | 99.84% | 99.46% | 258.0 | 10080.2 | 3000ms | 10/1835 |
| ✅ | `agify_name` | 99.89% | 99.73% | 391.3 | 16112.2 | 2000ms | 5/1835 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.89% | 196.2 | 3882.8 | 2000ms | 2/1835 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5124.8 | 70.0% |
| `numbers_trivia` | 03:00 | 4867.8 | 48.65% |
| `nasa_apod` | 05:00 | 4572.2 | 62.79% |
| `nasa_apod` | 03:00 | 4105.3 | 62.16% |
| `numbers_trivia` | 10:00 | 3824.0 | 36.23% |
| `nasa_apod` | 17:00 | 3760.8 | 50.54% |
| `nasa_apod` | 09:00 | 3705.3 | 51.32% |
| `nasa_apod` | 11:00 | 3673.0 | 51.49% |
| `numbers_trivia` | 14:00 | 3528.9 | 34.15% |
| `nasa_apod` | 01:00 | 3333.4 | 48.21% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
