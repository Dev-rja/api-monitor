# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 06:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.8 | 588.9 | 1000ms | 0/147 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.2 | 234.1 | 1500ms | 0/147 |
| ❌ | `nasa_apod` | 90.48% | 70.75% | 1682.3 | 10538.0 | 2000ms | 43/147 |
| ❌ | `ipapi_check` | 93.2% | 100.0% | 156.2 | 252.2 | 2500ms | 0/147 |
| ❌ | `open_meteo_weather` | 94.56% | 95.24% | 998.0 | 14877.1 | 2000ms | 7/147 |
| ❌ | `dog_ceo_random` | 98.64% | 72.79% | 1709.3 | 5586.8 | 2500ms | 40/147 |
| ⚠️ | `useless_fact` | 98.64% | 99.32% | 622.6 | 10229.6 | 2500ms | 1/147 |
| ⚠️ | `catfact_random` | 98.64% | 99.32% | 301.6 | 10070.5 | 3000ms | 1/147 |
| ✅ | `agify_name` | 100.0% | 99.32% | 405.6 | 3237.1 | 2000ms | 1/147 |
| ✅ | `rest_countries` | 100.0% | 98.64% | 299.9 | 7269.1 | 2500ms | 2/147 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.32% | 250.0 | 2314.9 | 2000ms | 1/147 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.8 | 252.0 | 1500ms | 0/147 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `open_meteo_weather` | 05:00 | 3474.6 | 20.0% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 3203.4 | 50.0% |
| `dog_ceo_random` | 12:00 | 3057.6 | 50.0% |
| `nasa_apod` | 20:00 | 2829.3 | 40.0% |
| `nasa_apod` | 22:00 | 2715.0 | 30.0% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
