# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 09:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **81.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.9 | 588.9 | 1000ms | 0/149 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.4 | 234.1 | 1500ms | 0/149 |
| ❌ | `nasa_apod` | 89.26% | 70.47% | 1681.7 | 10538.0 | 2000ms | 44/149 |
| ❌ | `ipapi_check` | 92.62% | 100.0% | 155.5 | 252.2 | 2500ms | 0/149 |
| ❌ | `open_meteo_weather` | 94.63% | 95.3% | 991.2 | 14877.1 | 2000ms | 7/149 |
| ❌ | `dog_ceo_random` | 98.66% | 73.15% | 1692.8 | 5586.8 | 2500ms | 40/149 |
| ⚠️ | `useless_fact` | 98.66% | 99.33% | 619.9 | 10229.6 | 2500ms | 1/149 |
| ⚠️ | `catfact_random` | 98.66% | 99.33% | 301.2 | 10070.5 | 3000ms | 1/149 |
| ✅ | `agify_name` | 100.0% | 99.33% | 407.5 | 3237.1 | 2000ms | 1/149 |
| ✅ | `rest_countries` | 100.0% | 98.66% | 298.4 | 7269.1 | 2500ms | 2/149 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.33% | 249.7 | 2314.9 | 2000ms | 1/149 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.9 | 252.0 | 1500ms | 0/149 |

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
