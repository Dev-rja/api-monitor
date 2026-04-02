# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 16:14 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **8/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 303.8 | 498.3 | 1000ms | 0/10 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 108.8 | 202.3 | 1500ms | 0/10 |
| ❌ | `dog_ceo_random` | 100.0% | 60.0% | 2233.5 | 4518.4 | 2500ms | 4/10 |
| ⚠️ | `nasa_apod` | 100.0% | 80.0% | 835.3 | 2644.3 | 2000ms | 2/10 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 585.7 | 804.5 | 2000ms | 0/10 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 576.8 | 829.9 | 2500ms | 0/10 |
| ✅ | `agify_name` | 100.0% | 100.0% | 466.8 | 733.3 | 2000ms | 0/10 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 288.1 | 737.9 | 2000ms | 0/10 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 219.0 | 411.7 | 3000ms | 0/10 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 196.1 | 300.4 | 2500ms | 0/10 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 158.2 | 248.6 | 2500ms | 0/10 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 96.0 | 195.8 | 1500ms | 0/10 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `dog_ceo_random` | 14:00 | 4518.4 | 100.0% |
| `dog_ceo_random` | 16:00 | 3016.7 | 100.0% |
| `dog_ceo_random` | 12:00 | 2811.7 | 100.0% |
| `dog_ceo_random` | 08:00 | 2743.5 | 100.0% |
| `nasa_apod` | 11:00 | 2644.3 | 100.0% |
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
