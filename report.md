# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 08:17 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **81.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.4 | 588.9 | 1000ms | 0/148 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 113.7 | 234.1 | 1500ms | 0/148 |
| ❌ | `nasa_apod` | 89.86% | 70.95% | 1675.5 | 10538.0 | 2000ms | 43/148 |
| ❌ | `ipapi_check` | 92.57% | 100.0% | 155.6 | 252.2 | 2500ms | 0/148 |
| ❌ | `open_meteo_weather` | 94.59% | 95.27% | 994.6 | 14877.1 | 2000ms | 7/148 |
| ❌ | `dog_ceo_random` | 98.65% | 72.97% | 1700.9 | 5586.8 | 2500ms | 40/148 |
| ⚠️ | `useless_fact` | 98.65% | 99.32% | 620.7 | 10229.6 | 2500ms | 1/148 |
| ⚠️ | `catfact_random` | 98.65% | 99.32% | 300.9 | 10070.5 | 3000ms | 1/148 |
| ✅ | `agify_name` | 100.0% | 99.32% | 405.1 | 3237.1 | 2000ms | 1/148 |
| ✅ | `rest_countries` | 100.0% | 98.65% | 298.6 | 7269.1 | 2500ms | 2/148 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.32% | 250.0 | 2314.9 | 2000ms | 1/148 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.1 | 252.0 | 1500ms | 0/148 |

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
