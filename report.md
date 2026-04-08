# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 00:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **81.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.0 | 588.9 | 1000ms | 0/144 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.5 | 234.1 | 1500ms | 0/144 |
| ❌ | `nasa_apod` | 91.67% | 70.14% | 1704.4 | 10538.0 | 2000ms | 43/144 |
| ❌ | `ipapi_check` | 93.06% | 100.0% | 156.0 | 252.2 | 2500ms | 0/144 |
| ❌ | `open_meteo_weather` | 94.44% | 95.14% | 1008.1 | 14877.1 | 2000ms | 7/144 |
| ❌ | `dog_ceo_random` | 98.61% | 72.22% | 1738.4 | 5586.8 | 2500ms | 40/144 |
| ⚠️ | `useless_fact` | 98.61% | 99.31% | 626.3 | 10229.6 | 2500ms | 1/144 |
| ⚠️ | `catfact_random` | 98.61% | 99.31% | 305.4 | 10070.5 | 3000ms | 1/144 |
| ✅ | `agify_name` | 100.0% | 99.31% | 407.8 | 3237.1 | 2000ms | 1/144 |
| ✅ | `rest_countries` | 100.0% | 98.61% | 301.8 | 7269.1 | 2500ms | 2/144 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.31% | 251.9 | 2314.9 | 2000ms | 1/144 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.3 | 252.0 | 1500ms | 0/144 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `useless_fact` | 03:00 | 5454.5 | 50.0% |
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `open_meteo_weather` | 05:00 | 4216.1 | 25.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 3203.4 | 50.0% |
| `open_meteo_weather` | 06:00 | 3112.1 | 20.0% |
| `dog_ceo_random` | 12:00 | 3057.6 | 50.0% |
| `nasa_apod` | 20:00 | 2829.3 | 40.0% |
| `nasa_apod` | 22:00 | 2715.0 | 30.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
