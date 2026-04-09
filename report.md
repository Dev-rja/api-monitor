# API Reliability Monitor — SLA Report

> Last updated: **2026-04-09 19:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.7 | 588.9 | 1000ms | 0/175 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 109.9 | 234.1 | 1500ms | 0/175 |
| ❌ | `nasa_apod` | 80.57% | 72.57% | 1637.4 | 10538.0 | 2000ms | 48/175 |
| ❌ | `ipapi_check` | 93.14% | 100.0% | 154.7 | 252.2 | 2500ms | 0/175 |
| ⚠️ | `open_meteo_weather` | 95.43% | 96.0% | 934.2 | 14877.1 | 2000ms | 7/175 |
| ❌ | `dog_ceo_random` | 98.86% | 77.14% | 1498.1 | 5586.8 | 2500ms | 40/175 |
| ⚠️ | `useless_fact` | 98.86% | 99.43% | 601.6 | 10229.6 | 2500ms | 1/175 |
| ⚠️ | `catfact_random` | 98.86% | 99.43% | 286.3 | 10070.5 | 3000ms | 1/175 |
| ✅ | `agify_name` | 100.0% | 99.43% | 402.8 | 3237.1 | 2000ms | 1/175 |
| ✅ | `rest_countries` | 100.0% | 98.86% | 288.7 | 7269.1 | 2500ms | 2/175 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.43% | 247.0 | 2314.9 | 2000ms | 1/175 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/175 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `nasa_apod` | 18:00 | 3358.5 | 57.14% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `nasa_apod` | 11:00 | 2771.9 | 41.67% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2672.7 | 36.36% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
