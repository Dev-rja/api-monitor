# API Reliability Monitor — SLA Report

> Last updated: **2026-04-23 21:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.57% | 4160.1 | 10206.7 | 1000ms | 179/454 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 129.1 | 4088.9 | 1500ms | 2/454 |
| ❌ | `nasa_apod` | 61.67% | 36.78% | 4399.6 | 10549.1 | 2000ms | 287/454 |
| ❌ | `ipapi_check` | 93.61% | 100.0% | 158.4 | 353.0 | 2500ms | 0/454 |
| ⚠️ | `open_meteo_weather` | 98.24% | 96.92% | 739.6 | 14877.1 | 2000ms | 14/454 |
| ⚠️ | `rest_countries` | 98.46% | 98.02% | 362.0 | 10221.5 | 2500ms | 9/454 |
| ⚠️ | `dog_ceo_random` | 99.34% | 90.75% | 836.7 | 10244.1 | 2500ms | 42/454 |
| ✅ | `catfact_random` | 99.34% | 99.34% | 269.1 | 10080.2 | 3000ms | 3/454 |
| ✅ | `useless_fact` | 99.56% | 99.12% | 583.4 | 10229.6 | 2500ms | 4/454 |
| ✅ | `agify_name` | 100.0% | 99.78% | 373.9 | 3237.1 | 2000ms | 1/454 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 233.2 | 2314.9 | 2000ms | 1/454 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/454 |

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
