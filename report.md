# API Reliability Monitor — SLA Report

> Last updated: **2026-07-23 09:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.12% | 1973.3 | 10353.0 | 1000ms | 277/1549 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 123.0 | 4595.4 | 1500ms | 4/1549 |
| ❌ | `ipapi_check` | 71.27% | 99.94% | 151.8 | 4507.0 | 2500ms | 1/1549 |
| ❌ | `nasa_apod` | 77.15% | 53.52% | 3066.0 | 11152.5 | 2000ms | 720/1549 |
| ⚠️ | `dog_ceo_random` | 95.16% | 96.32% | 560.0 | 10244.1 | 2500ms | 57/1549 |
| ⚠️ | `open_meteo_weather` | 98.77% | 97.35% | 710.9 | 14877.1 | 2000ms | 41/1549 |
| ✅ | `rest_countries` | 99.03% | 98.71% | 302.4 | 10221.5 | 2500ms | 20/1549 |
| ✅ | `useless_fact` | 99.68% | 99.74% | 637.3 | 10229.6 | 2500ms | 4/1549 |
| ✅ | `catfact_random` | 99.81% | 99.42% | 256.7 | 10080.2 | 3000ms | 9/1549 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.8 | 4328.4 | 1500ms | 1/1549 |
| ✅ | `agify_name` | 99.94% | 99.74% | 386.2 | 16112.2 | 2000ms | 4/1549 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 203.2 | 3882.8 | 2000ms | 2/1549 |

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
| `nasa_apod` | 11:00 | 3420.6 | 50.0% |
| `numbers_trivia` | 03:00 | 3417.3 | 32.0% |
| `nasa_apod` | 18:00 | 3322.0 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
