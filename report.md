# API Reliability Monitor — SLA Report

> Last updated: **2026-04-23 09:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 61.8% | 4040.3 | 10206.7 | 1000ms | 170/445 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.8 | 4088.9 | 1500ms | 2/445 |
| ❌ | `nasa_apod` | 61.57% | 37.08% | 4385.9 | 10549.1 | 2000ms | 280/445 |
| ❌ | `ipapi_check` | 93.71% | 100.0% | 158.2 | 353.0 | 2500ms | 0/445 |
| ⚠️ | `open_meteo_weather` | 98.2% | 96.85% | 744.3 | 14877.1 | 2000ms | 14/445 |
| ⚠️ | `rest_countries` | 98.43% | 98.2% | 346.8 | 10221.5 | 2500ms | 8/445 |
| ⚠️ | `dog_ceo_random` | 99.33% | 90.56% | 846.2 | 10244.1 | 2500ms | 42/445 |
| ✅ | `catfact_random` | 99.33% | 99.33% | 270.6 | 10080.2 | 3000ms | 3/445 |
| ✅ | `useless_fact` | 99.55% | 99.1% | 585.7 | 10229.6 | 2500ms | 4/445 |
| ✅ | `agify_name` | 100.0% | 99.78% | 375.7 | 3237.1 | 2000ms | 1/445 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 233.7 | 2314.9 | 2000ms | 1/445 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/445 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 6132.0 | 73.08% |
| `nasa_apod` | 03:00 | 5851.5 | 84.62% |
| `nasa_apod` | 18:00 | 5700.0 | 84.21% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 4979.2 | 61.54% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `nasa_apod` | 21:00 | 4923.2 | 56.0% |
| `numbers_trivia` | 07:00 | 4886.6 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
