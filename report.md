# API Reliability Monitor — SLA Report

> Last updated: **2026-07-23 16:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.1% | 1973.3 | 10353.0 | 1000ms | 278/1553 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 123.0 | 4595.4 | 1500ms | 4/1553 |
| ❌ | `ipapi_check` | 71.22% | 99.94% | 151.8 | 4507.0 | 2500ms | 1/1553 |
| ❌ | `nasa_apod` | 77.14% | 53.44% | 3068.0 | 11152.5 | 2000ms | 723/1553 |
| ⚠️ | `dog_ceo_random` | 95.17% | 96.33% | 559.5 | 10244.1 | 2500ms | 57/1553 |
| ⚠️ | `open_meteo_weather` | 98.78% | 97.36% | 710.6 | 14877.1 | 2000ms | 41/1553 |
| ✅ | `rest_countries` | 99.03% | 98.71% | 302.0 | 10221.5 | 2500ms | 20/1553 |
| ✅ | `useless_fact` | 99.68% | 99.74% | 637.7 | 10229.6 | 2500ms | 4/1553 |
| ✅ | `catfact_random` | 99.81% | 99.42% | 256.5 | 10080.2 | 3000ms | 9/1553 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.7 | 4328.4 | 1500ms | 1/1553 |
| ✅ | `agify_name` | 99.87% | 99.74% | 386.3 | 16112.2 | 2000ms | 4/1553 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 203.1 | 3882.8 | 2000ms | 2/1553 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4182.2 | 72.0% |
| `nasa_apod` | 17:00 | 3796.8 | 51.9% |
| `nasa_apod` | 09:00 | 3768.6 | 50.0% |
| `nasa_apod` | 12:00 | 3432.5 | 52.24% |
| `nasa_apod` | 01:00 | 3423.8 | 48.98% |
| `numbers_trivia` | 03:00 | 3417.3 | 32.0% |
| `nasa_apod` | 11:00 | 3406.9 | 50.57% |
| `nasa_apod` | 18:00 | 3322.0 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
