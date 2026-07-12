# API Reliability Monitor — SLA Report

> Last updated: **2026-07-12 11:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.76% | 2122.5 | 10206.7 | 1000ms | 267/1388 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.5 | 4595.4 | 1500ms | 4/1388 |
| ❌ | `nasa_apod` | 75.0% | 50.58% | 3285.4 | 11152.5 | 2000ms | 686/1388 |
| ❌ | `ipapi_check` | 75.22% | 99.93% | 154.2 | 4507.0 | 2500ms | 1/1388 |
| ❌ | `dog_ceo_random` | 94.74% | 96.61% | 541.3 | 10244.1 | 2500ms | 47/1388 |
| ⚠️ | `open_meteo_weather` | 98.63% | 97.05% | 727.1 | 14877.1 | 2000ms | 41/1388 |
| ⚠️ | `rest_countries` | 98.92% | 98.63% | 312.8 | 10221.5 | 2500ms | 19/1388 |
| ✅ | `useless_fact` | 99.64% | 99.71% | 634.3 | 10229.6 | 2500ms | 4/1388 |
| ✅ | `catfact_random` | 99.78% | 99.35% | 256.1 | 10080.2 | 3000ms | 9/1388 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.9 | 4328.4 | 1500ms | 1/1388 |
| ✅ | `agify_name` | 99.93% | 99.71% | 385.7 | 16112.2 | 2000ms | 4/1388 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 210.1 | 3882.8 | 2000ms | 2/1388 |

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
| `nasa_apod` | 20:00 | 3509.2 | 51.14% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
