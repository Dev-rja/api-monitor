# API Reliability Monitor — SLA Report

> Last updated: **2026-07-19 09:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.12% | 1988.9 | 10206.7 | 1000ms | 267/1493 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.8 | 4595.4 | 1500ms | 4/1493 |
| ❌ | `ipapi_check` | 72.94% | 99.93% | 152.7 | 4507.0 | 2500ms | 1/1493 |
| ❌ | `nasa_apod` | 76.29% | 52.11% | 3156.4 | 11152.5 | 2000ms | 715/1493 |
| ⚠️ | `dog_ceo_random` | 95.04% | 96.25% | 562.4 | 10244.1 | 2500ms | 56/1493 |
| ⚠️ | `open_meteo_weather` | 98.73% | 97.25% | 715.2 | 14877.1 | 2000ms | 41/1493 |
| ✅ | `rest_countries` | 99.0% | 98.73% | 304.1 | 10221.5 | 2500ms | 19/1493 |
| ✅ | `useless_fact` | 99.67% | 99.73% | 635.7 | 10229.6 | 2500ms | 4/1493 |
| ✅ | `catfact_random` | 99.8% | 99.4% | 255.6 | 10080.2 | 3000ms | 9/1493 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 96.9 | 4328.4 | 1500ms | 1/1493 |
| ✅ | `agify_name` | 99.93% | 99.73% | 384.9 | 16112.2 | 2000ms | 4/1493 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 205.4 | 3882.8 | 2000ms | 2/1493 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4339.2 | 75.0% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 3891.8 | 50.79% |
| `nasa_apod` | 17:00 | 3889.4 | 53.25% |
| `nasa_apod` | 01:00 | 3614.7 | 52.17% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 11:00 | 3533.7 | 51.81% |
| `nasa_apod` | 12:00 | 3524.9 | 53.85% |
| `nasa_apod` | 18:00 | 3445.4 | 48.75% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
