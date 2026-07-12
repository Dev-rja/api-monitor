# API Reliability Monitor — SLA Report

> Last updated: **2026-07-12 19:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.86% | 2112.8 | 10206.7 | 1000ms | 267/1395 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.4 | 4595.4 | 1500ms | 4/1395 |
| ❌ | `ipapi_check` | 74.98% | 99.93% | 154.1 | 4507.0 | 2500ms | 1/1395 |
| ❌ | `nasa_apod` | 75.13% | 50.82% | 3271.1 | 11152.5 | 2000ms | 686/1395 |
| ❌ | `dog_ceo_random` | 94.77% | 96.56% | 543.5 | 10244.1 | 2500ms | 48/1395 |
| ⚠️ | `open_meteo_weather` | 98.64% | 97.06% | 726.0 | 14877.1 | 2000ms | 41/1395 |
| ⚠️ | `rest_countries` | 98.92% | 98.64% | 312.1 | 10221.5 | 2500ms | 19/1395 |
| ✅ | `useless_fact` | 99.64% | 99.71% | 634.1 | 10229.6 | 2500ms | 4/1395 |
| ✅ | `catfact_random` | 99.78% | 99.35% | 255.8 | 10080.2 | 3000ms | 9/1395 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.7 | 4328.4 | 1500ms | 1/1395 |
| ✅ | `agify_name` | 99.93% | 99.71% | 385.3 | 16112.2 | 2000ms | 4/1395 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 209.6 | 3882.8 | 2000ms | 2/1395 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 09:00 | 4062.5 | 53.33% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4055.0 | 54.79% |
| `nasa_apod` | 01:00 | 3862.2 | 54.76% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 18:00 | 3664.0 | 51.35% |
| `nasa_apod` | 12:00 | 3605.8 | 53.23% |
| `nasa_apod` | 20:00 | 3509.2 | 51.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
