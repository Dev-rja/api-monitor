# API Reliability Monitor — SLA Report

> Last updated: **2026-06-10 12:14 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.74% | 2718.4 | 10206.7 | 1000ms | 266/1053 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.7 | 4595.4 | 1500ms | 4/1053 |
| ❌ | `ipapi_check` | 76.16% | 99.91% | 156.5 | 4507.0 | 2500ms | 1/1053 |
| ❌ | `nasa_apod` | 76.26% | 55.18% | 3077.6 | 10565.8 | 2000ms | 472/1053 |
| ⚠️ | `rest_countries` | 98.58% | 98.29% | 348.5 | 10221.5 | 2500ms | 18/1053 |
| ⚠️ | `open_meteo_weather` | 98.96% | 96.96% | 702.9 | 14877.1 | 2000ms | 32/1053 |
| ✅ | `dog_ceo_random` | 99.53% | 96.01% | 570.1 | 10244.1 | 2500ms | 42/1053 |
| ✅ | `catfact_random` | 99.72% | 99.15% | 265.8 | 10080.2 | 3000ms | 9/1053 |
| ✅ | `coingecko_bitcoin` | 99.72% | 100.0% | 96.7 | 253.3 | 1500ms | 0/1053 |
| ✅ | `useless_fact` | 99.81% | 99.62% | 623.5 | 10229.6 | 2500ms | 4/1053 |
| ✅ | `agify_name` | 99.91% | 99.72% | 380.0 | 16112.2 | 2000ms | 3/1053 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 221.1 | 3882.8 | 2000ms | 2/1053 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4039.6 | 52.54% |
| `nasa_apod` | 05:00 | 3993.8 | 64.29% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 11:00 | 3771.4 | 48.28% |
| `nasa_apod` | 01:00 | 3603.5 | 45.45% |
| `nasa_apod` | 12:00 | 3440.1 | 47.92% |
| `numbers_trivia` | 05:00 | 3427.1 | 32.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
