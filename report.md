# API Reliability Monitor — SLA Report

> Last updated: **2026-07-18 22:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.06% | 1994.5 | 10206.7 | 1000ms | 267/1488 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.6 | 4595.4 | 1500ms | 4/1488 |
| ❌ | `ipapi_check` | 73.12% | 99.93% | 152.9 | 4507.0 | 2500ms | 1/1488 |
| ❌ | `nasa_apod` | 76.21% | 52.02% | 3164.3 | 11152.5 | 2000ms | 714/1488 |
| ⚠️ | `dog_ceo_random` | 95.03% | 96.24% | 562.9 | 10244.1 | 2500ms | 56/1488 |
| ⚠️ | `open_meteo_weather` | 98.72% | 97.24% | 715.5 | 14877.1 | 2000ms | 41/1488 |
| ⚠️ | `rest_countries` | 98.99% | 98.72% | 304.4 | 10221.5 | 2500ms | 19/1488 |
| ✅ | `useless_fact` | 99.66% | 99.73% | 635.3 | 10229.6 | 2500ms | 4/1488 |
| ✅ | `catfact_random` | 99.8% | 99.4% | 255.4 | 10080.2 | 3000ms | 9/1488 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 96.9 | 4328.4 | 1500ms | 1/1488 |
| ✅ | `agify_name` | 99.93% | 99.73% | 384.8 | 16112.2 | 2000ms | 4/1488 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 205.6 | 3882.8 | 2000ms | 2/1488 |

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
