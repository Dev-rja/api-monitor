# API Reliability Monitor — SLA Report

> Last updated: **2026-07-18 20:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.03% | 1997.0 | 10206.7 | 1000ms | 267/1486 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.5 | 4595.4 | 1500ms | 4/1486 |
| ❌ | `ipapi_check` | 73.15% | 99.93% | 152.8 | 4507.0 | 2500ms | 1/1486 |
| ❌ | `nasa_apod` | 76.18% | 52.02% | 3166.5 | 11152.5 | 2000ms | 713/1486 |
| ⚠️ | `dog_ceo_random` | 95.02% | 96.23% | 562.6 | 10244.1 | 2500ms | 56/1486 |
| ⚠️ | `open_meteo_weather` | 98.72% | 97.24% | 715.6 | 14877.1 | 2000ms | 41/1486 |
| ⚠️ | `rest_countries` | 98.99% | 98.72% | 304.5 | 10221.5 | 2500ms | 19/1486 |
| ✅ | `useless_fact` | 99.66% | 99.73% | 635.4 | 10229.6 | 2500ms | 4/1486 |
| ✅ | `catfact_random` | 99.8% | 99.39% | 255.4 | 10080.2 | 3000ms | 9/1486 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 96.9 | 4328.4 | 1500ms | 1/1486 |
| ✅ | `agify_name` | 99.93% | 99.73% | 384.9 | 16112.2 | 2000ms | 4/1486 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 205.6 | 3882.8 | 2000ms | 2/1486 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4339.2 | 75.0% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 3947.4 | 51.61% |
| `nasa_apod` | 17:00 | 3889.4 | 53.25% |
| `nasa_apod` | 01:00 | 3686.6 | 53.33% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 11:00 | 3533.7 | 51.81% |
| `nasa_apod` | 12:00 | 3524.9 | 53.85% |
| `nasa_apod` | 18:00 | 3445.4 | 48.75% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
