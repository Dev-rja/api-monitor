# API Reliability Monitor — SLA Report

> Last updated: **2026-04-23 22:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.44% | 4173.0 | 10206.7 | 1000ms | 180/455 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 128.9 | 4088.9 | 1500ms | 2/455 |
| ❌ | `nasa_apod` | 61.54% | 36.7% | 4412.1 | 10549.1 | 2000ms | 288/455 |
| ❌ | `ipapi_check` | 93.63% | 100.0% | 158.3 | 353.0 | 2500ms | 0/455 |
| ⚠️ | `open_meteo_weather` | 98.24% | 96.92% | 739.5 | 14877.1 | 2000ms | 14/455 |
| ⚠️ | `rest_countries` | 98.46% | 98.02% | 361.8 | 10221.5 | 2500ms | 9/455 |
| ⚠️ | `dog_ceo_random` | 99.34% | 90.77% | 835.9 | 10244.1 | 2500ms | 42/455 |
| ✅ | `catfact_random` | 99.34% | 99.34% | 268.9 | 10080.2 | 3000ms | 3/455 |
| ✅ | `useless_fact` | 99.56% | 99.12% | 583.3 | 10229.6 | 2500ms | 4/455 |
| ✅ | `agify_name` | 100.0% | 99.78% | 374.2 | 3237.1 | 2000ms | 1/455 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 232.9 | 2314.9 | 2000ms | 1/455 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/455 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 6006.5 | 74.07% |
| `nasa_apod` | 18:00 | 5937.8 | 85.0% |
| `nasa_apod` | 03:00 | 5851.5 | 84.62% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5177.6 | 62.96% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 10:00 | 4947.7 | 47.62% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `numbers_trivia` | 07:00 | 4886.6 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
