# API Reliability Monitor — SLA Report

> Last updated: **2026-04-10 20:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 311.2 | 588.9 | 1000ms | 0/196 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.9 | 429.6 | 1500ms | 0/196 |
| ❌ | `nasa_apod` | 79.08% | 65.31% | 2011.6 | 10538.0 | 2000ms | 68/196 |
| ❌ | `ipapi_check` | 93.37% | 100.0% | 154.3 | 252.2 | 2500ms | 0/196 |
| ⚠️ | `open_meteo_weather` | 95.92% | 95.92% | 914.0 | 14877.1 | 2000ms | 8/196 |
| ❌ | `dog_ceo_random` | 98.98% | 79.59% | 1379.7 | 5586.8 | 2500ms | 40/196 |
| ⚠️ | `useless_fact` | 98.98% | 99.49% | 595.1 | 10229.6 | 2500ms | 1/196 |
| ⚠️ | `catfact_random` | 98.98% | 99.49% | 273.1 | 10070.5 | 3000ms | 1/196 |
| ✅ | `agify_name` | 100.0% | 99.49% | 404.2 | 3237.1 | 2000ms | 1/196 |
| ✅ | `rest_countries` | 100.0% | 98.47% | 302.7 | 7269.1 | 2500ms | 3/196 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.49% | 247.0 | 2314.9 | 2000ms | 1/196 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.5 | 252.0 | 1500ms | 0/196 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `dog_ceo_random` | 13:00 | 3433.6 | 80.0% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 13:00 | 3087.8 | 60.0% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `nasa_apod` | 22:00 | 2903.8 | 33.33% |
| `nasa_apod` | 15:00 | 2841.7 | 40.0% |
| `nasa_apod` | 11:00 | 2750.4 | 46.15% |
| `nasa_apod` | 20:00 | 2629.6 | 46.15% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
