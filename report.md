# API Reliability Monitor — SLA Report

> Last updated: **2026-04-23 11:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 61.52% | 4067.4 | 10206.7 | 1000ms | 172/447 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.8 | 4088.9 | 1500ms | 2/447 |
| ❌ | `nasa_apod` | 61.52% | 36.91% | 4395.2 | 10549.1 | 2000ms | 282/447 |
| ❌ | `ipapi_check` | 93.51% | 100.0% | 158.1 | 353.0 | 2500ms | 0/447 |
| ⚠️ | `open_meteo_weather` | 98.21% | 96.87% | 743.0 | 14877.1 | 2000ms | 14/447 |
| ⚠️ | `rest_countries` | 98.43% | 97.99% | 364.8 | 10221.5 | 2500ms | 9/447 |
| ⚠️ | `dog_ceo_random` | 99.33% | 90.6% | 844.3 | 10244.1 | 2500ms | 42/447 |
| ✅ | `catfact_random` | 99.33% | 99.33% | 269.8 | 10080.2 | 3000ms | 3/447 |
| ✅ | `useless_fact` | 99.55% | 99.11% | 585.1 | 10229.6 | 2500ms | 4/447 |
| ✅ | `agify_name` | 100.0% | 99.78% | 375.2 | 3237.1 | 2000ms | 1/447 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 233.7 | 2314.9 | 2000ms | 1/447 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/447 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 6132.0 | 73.08% |
| `nasa_apod` | 03:00 | 5851.5 | 84.62% |
| `nasa_apod` | 18:00 | 5700.0 | 84.21% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5177.6 | 62.96% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 10:00 | 4947.7 | 47.62% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `nasa_apod` | 21:00 | 4923.2 | 56.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
