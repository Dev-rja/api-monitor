# API Reliability Monitor — SLA Report

> Last updated: **2026-04-03 02:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 293.8 | 498.3 | 1000ms | 0/21 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 100.2 | 202.3 | 1500ms | 0/21 |
| ❌ | `dog_ceo_random` | 100.0% | 76.19% | 1659.6 | 4785.5 | 2500ms | 5/21 |
| ❌ | `nasa_apod` | 100.0% | 71.43% | 1048.3 | 2697.2 | 2000ms | 6/21 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 557.7 | 829.9 | 2500ms | 0/21 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 550.1 | 804.5 | 2000ms | 0/21 |
| ✅ | `agify_name` | 100.0% | 95.24% | 546.2 | 3237.1 | 2000ms | 1/21 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 244.2 | 474.2 | 3000ms | 0/21 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 242.7 | 737.9 | 2000ms | 0/21 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 204.2 | 363.3 | 2500ms | 0/21 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 167.9 | 248.6 | 2500ms | 0/21 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 104.1 | 195.8 | 1500ms | 0/21 |

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
