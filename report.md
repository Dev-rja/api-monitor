# API Reliability Monitor — SLA Report

> Last updated: **2026-04-02 07:26 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **9/12** &nbsp;|&nbsp; Avg uptime: **83.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 358.2 | 440.2 | 1000ms | 0/2 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 47.3 | 59.9 | 1500ms | 0/2 |
| ✅ | `dog_ceo_random` | 100.0% | 100.0% | 1706.6 | 1899.6 | 2500ms | 0/2 |
| ❌ | `nasa_apod` | 100.0% | 50.0% | 1394.6 | 2530.3 | 2000ms | 1/2 |
| ✅ | `open_meteo_weather` | 100.0% | 100.0% | 617.6 | 648.9 | 2000ms | 0/2 |
| ✅ | `useless_fact` | 100.0% | 100.0% | 608.7 | 660.7 | 2500ms | 0/2 |
| ✅ | `agify_name` | 100.0% | 100.0% | 532.8 | 578.9 | 2000ms | 0/2 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 100.0% | 261.0 | 284.7 | 2000ms | 0/2 |
| ✅ | `rest_countries` | 100.0% | 100.0% | 250.5 | 269.7 | 2500ms | 0/2 |
| ✅ | `catfact_random` | 100.0% | 100.0% | 236.0 | 292.6 | 3000ms | 0/2 |
| ✅ | `ipapi_check` | 100.0% | 100.0% | 141.1 | 188.1 | 2500ms | 0/2 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 120.8 | 124.5 | 1500ms | 0/2 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 07:00 | 2530.3 | 100.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
