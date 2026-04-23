# API Reliability Monitor — SLA Report

> Last updated: **2026-04-23 21:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.71% | 4147.1 | 10206.7 | 1000ms | 178/453 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 129.3 | 4088.9 | 1500ms | 2/453 |
| ❌ | `nasa_apod` | 61.59% | 36.64% | 4408.2 | 10549.1 | 2000ms | 287/453 |
| ❌ | `ipapi_check` | 93.6% | 100.0% | 158.4 | 353.0 | 2500ms | 0/453 |
| ⚠️ | `open_meteo_weather` | 98.23% | 96.91% | 740.2 | 14877.1 | 2000ms | 14/453 |
| ⚠️ | `rest_countries` | 98.45% | 98.01% | 362.3 | 10221.5 | 2500ms | 9/453 |
| ⚠️ | `dog_ceo_random` | 99.34% | 90.73% | 837.7 | 10244.1 | 2500ms | 42/453 |
| ✅ | `catfact_random` | 99.34% | 99.34% | 267.7 | 10080.2 | 3000ms | 3/453 |
| ✅ | `useless_fact` | 99.56% | 99.12% | 583.6 | 10229.6 | 2500ms | 4/453 |
| ✅ | `agify_name` | 100.0% | 99.78% | 373.9 | 3237.1 | 2000ms | 1/453 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 233.2 | 2314.9 | 2000ms | 1/453 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.2 | 252.0 | 1500ms | 0/453 |

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
