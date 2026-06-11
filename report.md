# API Reliability Monitor — SLA Report

> Last updated: **2026-06-11 06:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.88% | 2704.0 | 10206.7 | 1000ms | 266/1059 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.8 | 4595.4 | 1500ms | 4/1059 |
| ❌ | `nasa_apod` | 76.2% | 54.86% | 3093.8 | 10565.8 | 2000ms | 478/1059 |
| ❌ | `ipapi_check` | 76.3% | 99.91% | 156.6 | 4507.0 | 2500ms | 1/1059 |
| ⚠️ | `rest_countries` | 98.58% | 98.3% | 347.5 | 10221.5 | 2500ms | 18/1059 |
| ⚠️ | `open_meteo_weather` | 98.96% | 96.79% | 709.5 | 14877.1 | 2000ms | 34/1059 |
| ✅ | `dog_ceo_random` | 99.53% | 96.03% | 570.7 | 10244.1 | 2500ms | 42/1059 |
| ✅ | `catfact_random` | 99.72% | 99.15% | 265.1 | 10080.2 | 3000ms | 9/1059 |
| ✅ | `coingecko_bitcoin` | 99.72% | 100.0% | 96.8 | 253.3 | 1500ms | 0/1059 |
| ✅ | `useless_fact` | 99.81% | 99.62% | 623.4 | 10229.6 | 2500ms | 4/1059 |
| ✅ | `agify_name` | 99.91% | 99.72% | 379.7 | 16112.2 | 2000ms | 3/1059 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 221.0 | 3882.8 | 2000ms | 2/1059 |

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
| `nasa_apod` | 01:00 | 3562.3 | 47.83% |
| `nasa_apod` | 12:00 | 3440.1 | 47.92% |
| `numbers_trivia` | 05:00 | 3427.1 | 32.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
