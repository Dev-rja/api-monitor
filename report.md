# API Reliability Monitor — SLA Report

> Last updated: **2026-04-10 15:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 310.8 | 588.9 | 1000ms | 0/191 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.7 | 429.6 | 1500ms | 0/191 |
| ❌ | `nasa_apod` | 79.58% | 67.02% | 1928.0 | 10538.0 | 2000ms | 63/191 |
| ❌ | `ipapi_check` | 93.19% | 100.0% | 153.9 | 252.2 | 2500ms | 0/191 |
| ⚠️ | `open_meteo_weather` | 95.81% | 95.81% | 922.9 | 14877.1 | 2000ms | 8/191 |
| ❌ | `dog_ceo_random` | 98.95% | 79.06% | 1407.3 | 5586.8 | 2500ms | 40/191 |
| ⚠️ | `useless_fact` | 98.95% | 99.48% | 597.6 | 10229.6 | 2500ms | 1/191 |
| ⚠️ | `catfact_random` | 98.95% | 99.48% | 275.3 | 10070.5 | 3000ms | 1/191 |
| ✅ | `agify_name` | 100.0% | 99.48% | 405.3 | 3237.1 | 2000ms | 1/191 |
| ✅ | `rest_countries` | 100.0% | 98.43% | 304.9 | 7269.1 | 2500ms | 3/191 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.48% | 247.8 | 2314.9 | 2000ms | 1/191 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.5 | 252.0 | 1500ms | 0/191 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `dog_ceo_random` | 13:00 | 3433.6 | 80.0% |
| `nasa_apod` | 18:00 | 3358.5 | 57.14% |
| `nasa_apod` | 13:00 | 3087.8 | 60.0% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `nasa_apod` | 22:00 | 2903.8 | 33.33% |
| `nasa_apod` | 15:00 | 2841.7 | 40.0% |
| `nasa_apod` | 11:00 | 2750.4 | 46.15% |
| `nasa_apod` | 20:00 | 2637.8 | 41.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
