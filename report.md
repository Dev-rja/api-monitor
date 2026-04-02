# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 22:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 289.5 | 498.3 | 1000ms | 0/18 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 106.5 | 202.3 | 1500ms | 0/18 |
| ❌ | `dog_ceo_random` | 100.0% | 72.22% | 1854.4 | 4785.5 | 2500ms | 5/18 |
| ❌ | `nasa_apod` | 100.0% | 72.22% | 1023.8 | 2649.0 | 2000ms | 5/18 |
| ⚠️ | `agify_name` | 100.0% | 94.44% | 563.4 | 3237.1 | 2000ms | 1/18 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 553.8 | 829.9 | 2500ms | 0/18 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 544.7 | 804.5 | 2000ms | 0/18 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 250.4 | 737.9 | 2000ms | 0/18 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 232.4 | 417.8 | 3000ms | 0/18 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 194.6 | 320.8 | 2500ms | 0/18 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 159.0 | 248.6 | 2500ms | 0/18 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.4 | 195.8 | 1500ms | 0/18 |

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
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 18:00 | 2630.6 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |
| `nasa_apod` | 20:00 | 2344.2 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
