# API Reliability Monitor — SLA Report

> Last updated: **2026-04-09 16:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.5 | 588.9 | 1000ms | 0/172 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 110.7 | 234.1 | 1500ms | 0/172 |
| ❌ | `nasa_apod` | 81.4% | 73.84% | 1568.0 | 10538.0 | 2000ms | 45/172 |
| ❌ | `ipapi_check` | 93.02% | 100.0% | 154.3 | 252.2 | 2500ms | 0/172 |
| ⚠️ | `open_meteo_weather` | 95.35% | 95.93% | 941.5 | 14877.1 | 2000ms | 7/172 |
| ❌ | `dog_ceo_random` | 98.84% | 76.74% | 1517.2 | 5586.8 | 2500ms | 40/172 |
| ⚠️ | `useless_fact` | 98.84% | 99.42% | 604.0 | 10229.6 | 2500ms | 1/172 |
| ⚠️ | `catfact_random` | 98.84% | 99.42% | 287.8 | 10070.5 | 3000ms | 1/172 |
| ✅ | `agify_name` | 100.0% | 99.42% | 404.7 | 3237.1 | 2000ms | 1/172 |
| ✅ | `rest_countries` | 100.0% | 98.84% | 289.8 | 7269.1 | 2500ms | 2/172 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.42% | 245.0 | 2314.9 | 2000ms | 1/172 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/172 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `nasa_apod` | 11:00 | 2771.9 | 41.67% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2672.7 | 36.36% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |
| `nasa_apod` | 18:00 | 2207.4 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
