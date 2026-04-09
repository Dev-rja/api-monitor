# API Reliability Monitor — SLA Report

> Last updated: **2026-04-09 11:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.4 | 588.9 | 1000ms | 0/169 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.5 | 234.1 | 1500ms | 0/169 |
| ❌ | `nasa_apod` | 81.66% | 73.96% | 1553.2 | 10538.0 | 2000ms | 44/169 |
| ❌ | `ipapi_check` | 92.9% | 100.0% | 154.2 | 252.2 | 2500ms | 0/169 |
| ⚠️ | `open_meteo_weather` | 95.27% | 95.86% | 947.1 | 14877.1 | 2000ms | 7/169 |
| ❌ | `dog_ceo_random` | 98.82% | 76.33% | 1537.6 | 5586.8 | 2500ms | 40/169 |
| ⚠️ | `useless_fact` | 98.82% | 99.41% | 604.6 | 10229.6 | 2500ms | 1/169 |
| ⚠️ | `catfact_random` | 98.82% | 99.41% | 288.4 | 10070.5 | 3000ms | 1/169 |
| ✅ | `agify_name` | 100.0% | 99.41% | 404.3 | 3237.1 | 2000ms | 1/169 |
| ✅ | `rest_countries` | 100.0% | 98.82% | 288.2 | 7269.1 | 2500ms | 2/169 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.41% | 245.6 | 2314.9 | 2000ms | 1/169 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.4 | 252.0 | 1500ms | 0/169 |

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
| `dog_ceo_random` | 12:00 | 2515.8 | 40.0% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
