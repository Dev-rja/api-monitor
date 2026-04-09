# API Reliability Monitor — SLA Report

> Last updated: **2026-04-09 10:20 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.1 | 588.9 | 1000ms | 0/168 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 111.2 | 234.1 | 1500ms | 0/168 |
| ❌ | `nasa_apod` | 81.55% | 73.81% | 1559.5 | 10538.0 | 2000ms | 44/168 |
| ❌ | `ipapi_check` | 92.86% | 100.0% | 154.4 | 252.2 | 2500ms | 0/168 |
| ⚠️ | `open_meteo_weather` | 95.24% | 95.83% | 949.7 | 14877.1 | 2000ms | 7/168 |
| ❌ | `dog_ceo_random` | 98.81% | 76.19% | 1544.5 | 5586.8 | 2500ms | 40/168 |
| ⚠️ | `useless_fact` | 98.81% | 99.4% | 605.1 | 10229.6 | 2500ms | 1/168 |
| ⚠️ | `catfact_random` | 98.81% | 99.4% | 289.5 | 10070.5 | 3000ms | 1/168 |
| ✅ | `agify_name` | 100.0% | 99.4% | 404.3 | 3237.1 | 2000ms | 1/168 |
| ✅ | `rest_countries` | 100.0% | 98.81% | 289.1 | 7269.1 | 2500ms | 2/168 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.4% | 246.4 | 2314.9 | 2000ms | 1/168 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.4 | 252.0 | 1500ms | 0/168 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 2978.7 | 45.45% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2672.7 | 36.36% |
| `dog_ceo_random` | 12:00 | 2515.8 | 40.0% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
