# API Reliability Monitor — SLA Report

> Last updated: **2026-07-24 15:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.8% | 1998.4 | 10353.0 | 1000ms | 285/1566 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 123.3 | 4595.4 | 1500ms | 4/1566 |
| ❌ | `ipapi_check` | 71.14% | 99.94% | 151.6 | 4507.0 | 2500ms | 1/1566 |
| ❌ | `nasa_apod` | 77.2% | 53.51% | 3053.3 | 11152.5 | 2000ms | 728/1566 |
| ⚠️ | `dog_ceo_random` | 95.15% | 96.36% | 557.8 | 10244.1 | 2500ms | 57/1566 |
| ⚠️ | `open_meteo_weather` | 98.79% | 97.38% | 709.6 | 14877.1 | 2000ms | 41/1566 |
| ✅ | `rest_countries` | 99.04% | 98.72% | 300.7 | 10221.5 | 2500ms | 20/1566 |
| ✅ | `useless_fact` | 99.68% | 99.74% | 638.0 | 10229.6 | 2500ms | 4/1566 |
| ✅ | `catfact_random` | 99.81% | 99.43% | 256.7 | 10080.2 | 3000ms | 9/1566 |
| ✅ | `coingecko_bitcoin` | 99.81% | 99.94% | 96.6 | 4328.4 | 1500ms | 1/1566 |
| ✅ | `agify_name` | 99.87% | 99.74% | 386.6 | 16112.2 | 2000ms | 4/1566 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 202.5 | 3882.8 | 2000ms | 2/1566 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4032.1 | 69.23% |
| `nasa_apod` | 17:00 | 3796.8 | 51.9% |
| `nasa_apod` | 09:00 | 3768.6 | 50.0% |
| `numbers_trivia` | 03:00 | 3679.6 | 34.62% |
| `nasa_apod` | 01:00 | 3423.8 | 48.98% |
| `nasa_apod` | 12:00 | 3420.1 | 52.94% |
| `nasa_apod` | 11:00 | 3406.9 | 50.57% |
| `nasa_apod` | 18:00 | 3286.5 | 47.06% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
