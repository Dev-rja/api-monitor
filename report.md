# API Reliability Monitor — SLA Report

> Last updated: **2026-06-11 11:07 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.91% | 2701.5 | 10206.7 | 1000ms | 266/1060 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.7 | 4595.4 | 1500ms | 4/1060 |
| ❌ | `nasa_apod` | 76.23% | 54.81% | 3093.3 | 10565.8 | 2000ms | 479/1060 |
| ❌ | `ipapi_check` | 76.32% | 99.91% | 156.6 | 4507.0 | 2500ms | 1/1060 |
| ⚠️ | `rest_countries` | 98.58% | 98.3% | 347.4 | 10221.5 | 2500ms | 18/1060 |
| ⚠️ | `open_meteo_weather` | 98.87% | 96.7% | 718.3 | 14877.1 | 2000ms | 35/1060 |
| ✅ | `dog_ceo_random` | 99.53% | 96.04% | 570.7 | 10244.1 | 2500ms | 42/1060 |
| ✅ | `catfact_random` | 99.72% | 99.15% | 264.9 | 10080.2 | 3000ms | 9/1060 |
| ✅ | `coingecko_bitcoin` | 99.72% | 100.0% | 96.7 | 253.3 | 1500ms | 0/1060 |
| ✅ | `useless_fact` | 99.81% | 99.62% | 623.4 | 10229.6 | 2500ms | 4/1060 |
| ✅ | `agify_name` | 99.91% | 99.72% | 379.5 | 16112.2 | 2000ms | 3/1060 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 220.9 | 3882.8 | 2000ms | 2/1060 |

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
| `nasa_apod` | 11:00 | 3751.1 | 49.15% |
| `nasa_apod` | 01:00 | 3562.3 | 47.83% |
| `nasa_apod` | 12:00 | 3440.1 | 47.92% |
| `numbers_trivia` | 05:00 | 3427.1 | 32.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
