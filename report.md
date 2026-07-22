# API Reliability Monitor — SLA Report

> Last updated: **2026-07-22 21:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.11% | 1972.9 | 10353.0 | 1000ms | 276/1543 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 123.1 | 4595.4 | 1500ms | 4/1543 |
| ❌ | `ipapi_check` | 71.48% | 99.94% | 152.0 | 4507.0 | 2500ms | 1/1543 |
| ❌ | `nasa_apod` | 77.06% | 53.4% | 3074.9 | 11152.5 | 2000ms | 719/1543 |
| ⚠️ | `dog_ceo_random` | 95.14% | 96.31% | 560.8 | 10244.1 | 2500ms | 57/1543 |
| ⚠️ | `open_meteo_weather` | 98.77% | 97.34% | 711.3 | 14877.1 | 2000ms | 41/1543 |
| ✅ | `rest_countries` | 99.03% | 98.7% | 302.8 | 10221.5 | 2500ms | 20/1543 |
| ✅ | `useless_fact` | 99.68% | 99.74% | 637.1 | 10229.6 | 2500ms | 4/1543 |
| ✅ | `catfact_random` | 99.81% | 99.42% | 257.0 | 10080.2 | 3000ms | 9/1543 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.9 | 4328.4 | 1500ms | 1/1543 |
| ✅ | `agify_name` | 99.94% | 99.74% | 386.0 | 16112.2 | 2000ms | 4/1543 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 203.5 | 3882.8 | 2000ms | 2/1543 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4182.2 | 72.0% |
| `nasa_apod` | 17:00 | 3796.8 | 51.9% |
| `nasa_apod` | 09:00 | 3789.7 | 49.23% |
| `nasa_apod` | 01:00 | 3487.7 | 50.0% |
| `nasa_apod` | 12:00 | 3432.5 | 52.24% |
| `nasa_apod` | 11:00 | 3420.6 | 50.0% |
| `numbers_trivia` | 03:00 | 3417.3 | 32.0% |
| `nasa_apod` | 18:00 | 3322.0 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
