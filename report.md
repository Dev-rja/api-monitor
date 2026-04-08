# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 10:43 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **81.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.6 | 588.9 | 1000ms | 0/150 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.1 | 234.1 | 1500ms | 0/150 |
| ❌ | `nasa_apod` | 88.67% | 70.67% | 1673.7 | 10538.0 | 2000ms | 44/150 |
| ❌ | `ipapi_check` | 92.67% | 100.0% | 155.3 | 252.2 | 2500ms | 0/150 |
| ❌ | `open_meteo_weather` | 94.67% | 95.33% | 988.7 | 14877.1 | 2000ms | 7/150 |
| ❌ | `dog_ceo_random` | 98.67% | 73.33% | 1684.0 | 5586.8 | 2500ms | 40/150 |
| ⚠️ | `useless_fact` | 98.67% | 99.33% | 619.1 | 10229.6 | 2500ms | 1/150 |
| ⚠️ | `catfact_random` | 98.67% | 99.33% | 300.8 | 10070.5 | 3000ms | 1/150 |
| ✅ | `agify_name` | 100.0% | 99.33% | 406.4 | 3237.1 | 2000ms | 1/150 |
| ✅ | `rest_countries` | 100.0% | 98.67% | 298.0 | 7269.1 | 2500ms | 2/150 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.33% | 249.7 | 2314.9 | 2000ms | 1/150 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.6 | 252.0 | 1500ms | 0/150 |

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
