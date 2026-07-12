# API Reliability Monitor — SLA Report

> Last updated: **2026-07-12 10:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.75% | 2123.9 | 10206.7 | 1000ms | 267/1387 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.5 | 4595.4 | 1500ms | 4/1387 |
| ❌ | `nasa_apod` | 74.98% | 50.54% | 3287.4 | 11152.5 | 2000ms | 686/1387 |
| ❌ | `ipapi_check` | 75.2% | 99.93% | 154.2 | 4507.0 | 2500ms | 1/1387 |
| ❌ | `dog_ceo_random` | 94.74% | 96.61% | 541.5 | 10244.1 | 2500ms | 47/1387 |
| ⚠️ | `open_meteo_weather` | 98.63% | 97.04% | 727.2 | 14877.1 | 2000ms | 41/1387 |
| ⚠️ | `rest_countries` | 98.92% | 98.63% | 312.9 | 10221.5 | 2500ms | 19/1387 |
| ✅ | `useless_fact` | 99.64% | 99.71% | 634.4 | 10229.6 | 2500ms | 4/1387 |
| ✅ | `catfact_random` | 99.78% | 99.35% | 256.0 | 10080.2 | 3000ms | 9/1387 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.8 | 4328.4 | 1500ms | 1/1387 |
| ✅ | `agify_name` | 99.93% | 99.71% | 385.6 | 16112.2 | 2000ms | 4/1387 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 210.1 | 3882.8 | 2000ms | 2/1387 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 17:00 | 4104.7 | 55.56% |
| `nasa_apod` | 09:00 | 4062.5 | 53.33% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 01:00 | 3862.2 | 54.76% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 18:00 | 3707.6 | 52.05% |
| `nasa_apod` | 12:00 | 3657.9 | 54.1% |
| `nasa_apod` | 11:00 | 3530.4 | 52.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
