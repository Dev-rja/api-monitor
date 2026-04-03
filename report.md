# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 06:14 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 283.1 | 498.3 | 1000ms | 0/23 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 102.0 | 202.3 | 1500ms | 0/23 |
| ❌ | `dog_ceo_random` | 100.0% | 78.26% | 1679.3 | 4785.5 | 2500ms | 5/23 |
| ❌ | `nasa_apod` | 100.0% | 73.91% | 1005.6 | 2697.2 | 2000ms | 6/23 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 549.7 | 829.9 | 2500ms | 0/23 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 539.0 | 804.5 | 2000ms | 0/23 |
| ✅ | `agify_name` | 100.0% | 95.65% | 520.9 | 3237.1 | 2000ms | 1/23 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 240.9 | 474.2 | 3000ms | 0/23 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 240.8 | 737.9 | 2000ms | 0/23 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 204.9 | 363.3 | 2500ms | 0/23 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 166.8 | 248.6 | 2500ms | 0/23 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 105.2 | 195.8 | 1500ms | 0/23 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 17:00 | 4785.5 | 100.0% |
| `dog_ceo_random` | 14:00 | 4518.4 | 100.0% |
| `agify_name` | 21:00 | 3237.1 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 02:00 | 2697.2 | 100.0% |
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
