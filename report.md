# API Reliability Monitor — SLA Report

> Last updated: **2026-04-12 18:31 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 304.5 | 588.9 | 1000ms | 0/247 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 129.8 | 3806.8 | 1500ms | 1/247 |
| ❌ | `nasa_apod` | 73.68% | 55.06% | 2821.8 | 10538.0 | 2000ms | 111/247 |
| ❌ | `ipapi_check` | 94.74% | 100.0% | 158.4 | 353.0 | 2500ms | 0/247 |
| ⚠️ | `open_meteo_weather` | 96.76% | 95.95% | 857.5 | 14877.1 | 2000ms | 10/247 |
| ⚠️ | `dog_ceo_random` | 99.19% | 83.4% | 1183.1 | 5586.8 | 2500ms | 41/247 |
| ✅ | `useless_fact` | 99.19% | 99.6% | 580.1 | 10229.6 | 2500ms | 1/247 |
| ✅ | `catfact_random` | 99.19% | 99.6% | 268.2 | 10070.5 | 3000ms | 1/247 |
| ✅ | `agify_name` | 100.0% | 99.6% | 388.9 | 3237.1 | 2000ms | 1/247 |
| ✅ | `rest_countries` | 100.0% | 98.79% | 286.4 | 7269.1 | 2500ms | 3/247 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.6% | 234.8 | 2314.9 | 2000ms | 1/247 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/247 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 18:00 | 3896.7 | 70.0% |
| `nasa_apod` | 13:00 | 3734.4 | 57.14% |
| `nasa_apod` | 20:00 | 3714.0 | 56.25% |
| `nasa_apod` | 03:00 | 3704.9 | 80.0% |
| `nasa_apod` | 17:00 | 3623.8 | 50.0% |
| `nasa_apod` | 14:00 | 3601.8 | 42.86% |
| `nasa_apod` | 08:00 | 3100.8 | 50.0% |
| `nasa_apod` | 19:00 | 3079.8 | 42.86% |
| `nasa_apod` | 22:00 | 2961.3 | 46.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
